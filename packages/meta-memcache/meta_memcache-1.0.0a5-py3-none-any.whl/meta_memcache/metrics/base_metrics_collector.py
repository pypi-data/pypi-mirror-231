import itertools
import threading
import time
from abc import ABC, abstractmethod
from collections import defaultdict
from typing import DefaultDict, Dict, Iterator, List


class BaseMetricsCollector(ABC):
    """
    Base class for metrics collectors. Subclasses should implement the _report()` method
    to integrate into the metrics system.`

    To be used as:
    * For counters:
    next(metrics_collector.counters[[key])
    * For metrics (latencies, num keys, etc.)
    metrics_collector.metrics[key].append(float_value)
    * For gauges (active conns, items in cache, etc.)
    metrics.gauges[key] = float_value
    """

    def __init__(self, prefix: str = "", collect_interval: int = 10) -> None:
        self._prefix = prefix
        self._collect_interval = collect_interval
        self._is_running = False
        self._worker = threading.Thread(
            target=self._collect,
            name="CacheMetricsCollector",
            daemon=True,
        )
        self.counters: DefaultDict[str, Iterator[int]] = defaultdict(
            lambda: itertools.count(start=1)
        )
        self.metrics: DefaultDict[str, List[float]] = defaultdict(list)
        self.gauges: DefaultDict[str, float] = defaultdict(float)
        self._total_metrics: DefaultDict[str, float] = defaultdict(float)

    def _collect(self) -> None:
        metrics: DefaultDict[str, List[float]] = defaultdict(list)
        while self._is_running:
            for k, v in metrics.items():
                self._total_metrics[k] += sum(v)
            self._report(
                counters=self.get_counters(),
                metrics=self.get_metrics(),
                gauges=self.get_gauges(),
            )
            # Swap the metrics instead of locking. Other threads might
            # race but they will either append to the old or new one
            # and will eventually get counted
            metrics, self.metrics = self.metrics, defaultdict(list)
            time.sleep(self._collect_interval)

    def get_counters(self) -> Dict[str, int]:
        return {
            self._prefix + k: int(v.__reduce__()[1][0]) - 1
            for k, v in self.counters.items()
        }

    def get_metrics(self) -> Dict[str, float]:
        return {self._prefix + k: v for k, v in self._total_metrics.items()}

    def get_gauges(self) -> Dict[str, float]:
        return {self._prefix + k: v for k, v in self.gauges.items()}

    @abstractmethod
    def _report(
        self,
        counters: Dict[str, int],
        metrics: Dict[str, float],
        gauges: Dict[str, float],
    ) -> None:
        ...  # pragma: no cover

    def start(self) -> None:
        if not self._is_running:
            self._is_running = True
            self._worker.start()

    def stop(self) -> None:
        self._is_running = False
