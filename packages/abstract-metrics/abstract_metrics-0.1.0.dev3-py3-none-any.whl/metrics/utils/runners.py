# Contains various metric runners

from typing import Enum, List, Union

from metrics import protocols
from metrics.types import OutputFormat


class BaseRunner:
    r"""Defines the base-runner for metrics generation."""


class MatrixRunner(BaseRunner):
    r"""A runner that builds & computes every metric for every application specified."""

    def run(
        self,
        metrics: protocols.ApplicationMetric | List[protocols.ApplicationMetric],
        applications: Union[
            List[protocols.Application], List[str], protocols.Application, str
        ],
        format: Enum = OutputFormat.LOG,
    ) -> List[protocols.ApplicationMetric]:
        r"""Builds & Runs metric generation."""

        if not isinstance(metrics, list):
            metrics = [metrics]

        if not isinstance(applications, list):
            applications = [applications]

        if not isinstance(format, OutputFormat):
            raise TypeError(
                f"Expected format type to be an {type(OutputFormat)}, got {type(format)}"
            )

        application_metrics = []
        for application in applications:
            # If string passed, convert to Application object.
            if isinstance(application, str):
                application = protocols.Application(name=application)

            for metric in metrics:
                metric = metric(application)
                metric.compute()
                application_metrics.append(metric)

                if format == OutputFormat.OUTPUT_FORMAT_LOG:
                    print(metric)
                    print(f"{metric.application.name:<20}: {metric.value:.1f}")

        return application_metrics
