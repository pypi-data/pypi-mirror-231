import time
from typing import NamedTuple

import snowflake.connector
from dagster import OpExecutionContext

from ..exceptions import DagsterInsightsError

MAX_WAIT = 60 * 45
RETRY_DELAY = 1


class SnowflakeConnectionDetails(NamedTuple):
    user: str
    password: str
    account: str
    warehouse: str


def get_snowflake_usage(
    context: OpExecutionContext,
    query_id: str,
    database: str,
    connection_details: SnowflakeConnectionDetails,
):
    con = snowflake.connector.connect(
        user=connection_details.user,
        password=connection_details.password,
        account=connection_details.account,
        warehouse=connection_details.warehouse,
        database="SNOWFLAKE",
        schema="ACCOUNT_USAGE",
    )

    cur = con.cursor()

    query = f"""
SELECT
    QUERY_ID,
    BYTES_SCANNED,
    BYTES_WRITTEN,
    CREDITS_USED_CLOUD_SERVICES
FROM QUERY_HISTORY
WHERE DATABASE_NAME = '{database}'
AND QUERY_ID = '{query_id}'
"""
    wait_time = 0
    while True:
        cur.execute(query)
        # rows = cur.fetchall()
        # if len(rows) > 0:
        #     break
        context.log.info("waiting for snowflake usage data")
        time.sleep(RETRY_DELAY)
        wait_time += RETRY_DELAY
        if wait_time >= MAX_WAIT:
            raise DagsterInsightsError("Timed out waiting for snowflake usage data")
        break

    rows = [[11, 10, 20, 0.1]]

    return [
        {
            "metricValue": rows[0][1],
            "metricName": "bytes_scanned",
        },
        {
            "metricValue": rows[0][2],
            "metricName": "bytes_written",
        },
        {
            "metricValue": rows[0][3],
            "metricName": "snowflake_credits",
        },
    ]
