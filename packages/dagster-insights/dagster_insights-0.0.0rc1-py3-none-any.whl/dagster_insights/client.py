from typing import Any, Dict, List, Optional

import dagster._check as check
import requests
import requests.exceptions
from dagster import OpExecutionContext
from dagster._annotations import experimental
from gql import Client, gql
from gql.transport import Transport
from gql.transport.requests import RequestsHTTPTransport

from .dbt import SnowflakeConnectionDetails, get_snowflake_usage
from .exceptions import DagsterInsightsError
from .model import DagsterInsightsMetric
from .query import PUT_CLOUD_METRICS_MUTATION


def chunks(chunk_list: list[Any], length: int):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(chunk_list), length):
        yield chunk_list[i : i + length]


@experimental
class DagsterInsightsClient:
    def __init__(
        self,
        organization_id: str,
        deployment: str,
        cloud_user_token: str,
        transport: Optional[Transport] = None,
        use_https: bool = False,
        timeout: int = 300,
        headers: Optional[Dict[str, str]] = None,
        snowflake_connection_details: Optional[SnowflakeConnectionDetails] = None,
    ):
        self._organization_id = check.str_param(organization_id, "organization_id")
        self._deployment = check.str_param(deployment, "deployment")
        check.str_param(cloud_user_token, "cloud_user_token")
        self._use_https = check.bool_param(use_https, "use_https")

        self._url = (
            ("https://" if self._use_https else "http://")
            + f"{self._organization_id}.dagster.cloud/{self._deployment}/graphql"
            + "/graphql"
        )
        if headers:
            headers["Dagster-Cloud-Api-Token"] = cloud_user_token
        else:
            headers = {"Dagster-Cloud-Api-Token": cloud_user_token}

        self._transport = check.opt_inst_param(
            transport,
            "transport",
            Transport,
            default=RequestsHTTPTransport(
                url=self._url, use_json=True, timeout=timeout, headers=headers
            ),
        )
        self._snowflake_connection_details = check.opt_inst_param(
            snowflake_connection_details,
            "snowflake_connection_details",
            SnowflakeConnectionDetails,
        )
        try:
            self._client = Client(transport=self._transport, fetch_schema_from_transport=True)
        except requests.exceptions.ConnectionError as exc:
            raise DagsterInsightsError(
                f"Error when connecting to url {self._url}. "
                + f"Did you specify organization id: {self._organization_id} "
                + f"and deployment: {self._deployment} "
                + "correctly?"
            ) from exc

    def _execute(self, query: str, variables: Optional[Dict[str, Any]] = None) -> dict[str, Any]:
        try:
            return self._client.execute(gql(query), variable_values=variables)
        except Exception as exc:  # catch generic Exception from the gql client
            raise DagsterInsightsError(
                f"Exception occured during execution of query \n{query}\n with variables"
                f" \n{variables}\n"
            ) from exc

    def put_context_metrics(
        self,
        context: OpExecutionContext,
        metrics: List[DagsterInsightsMetric],
    ) -> None:
        """Store metrics in the dagster cloud metrics store. This method is useful when you would like to
        store run, asset or asset group materialization metric data to view in the insights UI.

        Currently only supported in Dagster Cloud

        Args:
            metrics (Mapping[str, Any]): metrics to store in the dagster metrics store
        """
        check.list_param(metrics, "metrics", of_type=DagsterInsightsMetric)
        check.inst_param(context, "context", OpExecutionContext)
        metric_graphql_inputs = []

        if context.dagster_run.external_job_origin is None:
            raise DagsterInsightsError("dagster run for this context has not started yet")

        if context.has_assets_def:
            for selected_asset_keys in chunks(list(context.selected_asset_keys), 5):
                metric_graphql_inputs.append(
                    {
                        "runId": context.run_id,
                        "stepKey": context.get_step_execution_context().step.key,
                        "codeLocationName": context.dagster_run.external_job_origin.location_name,
                        "repositoryName": (
                            context.dagster_run.external_job_origin.external_repository_origin.repository_name
                        ),
                        "assetMetricDefinitions": [
                            {
                                "assetKey": selected_asset_key.to_python_identifier(),
                                "assetGroup": context.assets_def.group_names_by_key.get(
                                    selected_asset_key, None
                                ),
                                "metricValues": [
                                    {
                                        "metricValue": metric_def.metric_value,
                                        "metricName": metric_def.metric_name,
                                    }
                                    for metric_def in metrics
                                ],
                            }
                            for selected_asset_key in selected_asset_keys
                        ],
                    }
                )
        else:
            metric_graphql_inputs.append(
                {
                    "runId": context.run_id,
                    "stepKey": context.get_step_execution_context().step.key,
                    "codeLocationName": context.dagster_run.external_job_origin.location_name,
                    "repositoryName": (
                        context.dagster_run.external_job_origin.external_repository_origin.repository_name
                    ),
                    "jobMetricDefinitions": [
                        {
                            "metricValues": [
                                {
                                    "metricValue": metric_def.metric_value,
                                    "metricName": metric_def.metric_name,
                                }
                                for metric_def in metrics
                            ],
                        }
                    ],
                }
            )
        for metric_graphql_inputs in chunks(metric_graphql_inputs, 5):
            result = self._execute(PUT_CLOUD_METRICS_MUTATION, {"metrics": metric_graphql_inputs})
            if (
                result["createOrUpdateExternalMetrics"]["__typename"]
                != "CreateOrUpdateExternalMetricsSuccess"
            ):
                context.log.warning(
                    "failed to store metrics with error"
                    f" {result['createOrUpdateExternalMetrics']['message']}"
                )

    def store_dbt_adapter_metrics(
        self,
        context: OpExecutionContext,
        manifest: Dict[Any, Any],
        run_results: Dict[Any, Any],
    ) -> None:
        check.inst_param(context, "context", OpExecutionContext)
        check.dict_param(manifest, "manifest")
        check.dict_param(run_results, "run_results")
        if manifest["metadata"]["dbt_schema_version"] not in [
            "https://schemas.getdbt.com/dbt/manifest/v10.json",
            "https://schemas.getdbt.com/dbt/manifest/v9.json",
        ]:
            context.log.warn(
                f"unexpected dbt schema version: {manifest['metadata']['dbt_schema_version']},"
                " required: https://schemas.getdbt.com/dbt/manifest/v10.json"
            )
            return
        if (
            run_results["metadata"]["dbt_schema_version"]
            != "https://schemas.getdbt.com/dbt/run-results/v4.json"
        ):
            context.log.warn(
                f"unexpected dbt schema version: {manifest['metadata']['dbt_schema_version']},"
                " required: https://schemas.getdbt.com/dbt/run-results/v4.json"
            )
            return
        if context.dagster_run.external_job_origin is None:
            raise DagsterInsightsError("dagster run for this context has not started yet")
        # store the manifest and run results somewhere
        assetMetricDefinitions = []
        for result in run_results["results"]:
            node = manifest["nodes"][result["unique_id"]]
            metric_values = []
            for adapter_response_key in result["adapter_response"]:
                if adapter_response_key in ["_message", "code"]:
                    continue
                if (
                    self._snowflake_connection_details
                    and adapter_response_key == "query_id"
                    and "database" in node
                ):
                    snowflake_metrics = get_snowflake_usage(
                        context=context,
                        query_id=result["adapter_response"][adapter_response_key],
                        database=node["database"],
                        connection_details=self._snowflake_connection_details,
                    )
                    metric_values.extend(snowflake_metrics)
            # selected_asset_key = f"{node['schema']}"
            # context.assets_def.group_names_by_key.get(selected_asset_key, "")
            assetKey = next(
                iter(
                    filter(
                        lambda asset_key: asset_key.path[-1] == node["name"],
                        context.selected_asset_keys,
                    )
                )
            )
            assetMetricDefinitions.append(
                {
                    "assetKey": assetKey.to_python_identifier(),
                    "assetGroup": context.assets_def.group_names_by_key.get(assetKey, None),
                    "metricValues": metric_values,
                }
            )
        metric_graphql_inputs = []
        for assetMetricDefinitions in chunks(assetMetricDefinitions, 5):
            metric_graphql_inputs.append(
                {
                    "runId": context.run_id,
                    "stepKey": context.get_step_execution_context().step.key,
                    "codeLocationName": context.dagster_run.external_job_origin.location_name,
                    "repositoryName": (
                        context.dagster_run.external_job_origin.external_repository_origin.repository_name
                    ),
                    "assetMetricDefinitions": assetMetricDefinitions,
                }
            )
        for metric_graphql_inputs in chunks(metric_graphql_inputs, 5):
            result = self._execute(PUT_CLOUD_METRICS_MUTATION, {"metrics": metric_graphql_inputs})
            if (
                result["createOrUpdateExternalMetrics"]["__typename"]
                != "CreateOrUpdateExternalMetricsSuccess"
            ):
                context.log.warning(
                    "failed to store metrics with error"
                    f" {result['createOrUpdateExternalMetrics']['message']}"
                )

        context.log.info("successfully stored metrics")
