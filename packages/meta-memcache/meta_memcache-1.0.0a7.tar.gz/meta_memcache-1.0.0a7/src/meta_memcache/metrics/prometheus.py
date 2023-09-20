from typing import Dict, List, Optional, Union

from prometheus_client import Counter, Gauge
from prometheus_client.registry import CollectorRegistry

from meta_memcache.metrics.base import BaseMetricsCollector, MetricDefinition


class PrometheusMetricsCollector(BaseMetricsCollector):
    def __init__(
        self,
        namespace: str = "",
        registry: Optional[CollectorRegistry] = None,
    ) -> None:
        super().__init__(namespace=namespace)
        self._registry = registry
        self._counters: Dict[str, Counter] = {}
        self._gauges: Dict[str, Gauge] = {}

    def init_metrics(
        self,
        metrics: List[MetricDefinition],
        gauges: List[MetricDefinition],
    ) -> None:
        for metric in metrics:
            self._counters[metric.name] = Counter(
                name=metric.name,
                documentation=metric.documentation,
                labelnames=metric.labelnames,
                registry=self._registry,
                namespace=self._namespace,
            )
        for gauge in gauges:
            self._gauges[gauge.name] = Gauge(
                name=gauge.name,
                documentation=gauge.documentation,
                labelnames=gauge.labelnames,
                registry=self._registry,
                namespace=self._namespace,
            )

    def metric_inc(
        self,
        key: str,
        value: Union[float, int] = 1,
        labels: Optional[Dict[str, str]] = None,
    ) -> None:
        (self._counters[key].labels(**labels) if labels else self._counters[key]).inc(
            value
        )

    def gauge_set(
        self,
        key: str,
        value: float,
        labels: Optional[Dict[str, str]] = None,
    ) -> None:
        (self._gauges[key].labels(**labels) if labels else self._gauges[key]).set(value)

    def get_counters(self) -> Dict[str, float]:
        counters: Dict[str, float] = {}
        for counter in self._counters.values():
            metric = list(counter.collect())[0]
            for sample in metric.samples:
                if sample.name == metric.name + "_total":
                    counters[metric.name] = sample.value

        for gauge in self._gauges.values():
            metric = list(gauge.collect())[0]
            for sample in metric.samples:
                if sample.name == metric.name:
                    counters[metric.name] = sample.value
        return counters
