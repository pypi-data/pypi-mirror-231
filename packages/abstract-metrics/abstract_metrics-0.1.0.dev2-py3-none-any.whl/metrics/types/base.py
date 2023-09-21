import datetime
from abc import ABC, abstractmethod
from typing import Any, Final, List, Optional


class Application(ABC):
    """Base class for an Application wrapper."""

    @abstractmethod
    def __init__(self, name: str):
        self.name = name


class ApplicationMetric(ABC):
    """Defines an Application specific Metric"""

    @abstractmethod
    def __init__(self, application: Application):
        """Initialies the metric with the application it is associated to."""
        self.application: Final[Application] = application
        self.computed_at: Optional[datetime.datetime] = None
        self.errors: List[Exception] = []
        self._value: Optional[Any] = None

    @property
    def value(self) -> Any:
        """Fixed value of the metric."""
        return self._value

    @value.setter
    def value(self, value: Any) -> None:
        r"""This set's the metric value and updates the computed_at timestamp."""
        self.computed_at = datetime.datetime.now()
        self._value = value

    @abstractmethod
    def compute(self) -> (bool, Any):
        ...

    def asdict(self) -> dict[str, Any]:
        return {
            "application": self.application.name,
            "metric": self.__class__.__name__,
            "computed_at": self.computed_at,
            "errors": self.errors,
            "value": self.value,
        }


class NumericApplicationMetric(ApplicationMetric):
    @property
    @abstractmethod
    def value(self) -> Optional[float]:
        return self._value

    def compute(self) -> (bool, Optional[float]):
        ...
