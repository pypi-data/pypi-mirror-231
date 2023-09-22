from typing import NamedTuple


class DagsterInsightsMetric(NamedTuple):
    """This class gives information about a Metric.

    Args:
        metric_name (str): name of the metric
        metric_value (float): value of the metric
    """

    metric_name: str
    metric_value: float
