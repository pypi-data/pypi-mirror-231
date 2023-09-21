# Contains all metric Protocols.

import datetime
from typing import Protocol


class Application(Protocol):
    """Base Protocol for an Application wrapper."""

    name: str


class ApplicationMetric(Protocol):
    """Base protocol for an Application Metric."""

    # The Application or Service to which the Metric Applies
    application: "Application"

    # This should be set to datetime.datetime.now() when compute() is called.
    computed_at: datetime.datetime | None

    # Stores errors that occured during the last computation.
    errors: list[Exception]

    @property
    def value(self) -> float | None:
        r"""Returns the computed metric value or None if not applicable."""
        ...

    def compute(self) -> bool:
        r"""A callable that (re)computes & stores the metric value.
        This method must handle all exceptions.

        Returns:
            bool: True if computation was successful, False otherwise.
        """
        ...
