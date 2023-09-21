import asyncio
import logging
from enum import Enum
from typing import List, Union

from metrics.types import OutputFormat
from metrics.types import base as t


class BaseRunner:
    r"""Defines the base-runner for metrics generation."""


class MatrixRunner(BaseRunner):
    r"""A runner that builds & computes every metric for every application specified."""

    def run_serial(
        self,
        metrics: List[t.ApplicationMetric],
        applications: Union[List[t.Application], List[str]],
        format: Enum = OutputFormat.OUTPUT_FORMAT_LOG,
    ) -> List[t.ApplicationMetric]:
        r"""Synchronous version of metric generation."""

        if not isinstance(format, OutputFormat):
            raise TypeError(
                f"Expected type to be `{type(OutputFormat)}`, got `{type(format)}`"
            )

        application_metrics = []
        for application in applications:
            if isinstance(application, str):
                application = t.Application(name=application)

            for Metric in metrics:
                metric = Metric(application)  # type: ignore
                metric.compute_and_set()
                application_metrics.append(metric)

                if format == OutputFormat.OUTPUT_FORMAT_LOG:
                    logging.info(
                        "%s/%s: %s",
                        application.name,
                        metric.__class__.__name__,
                        metric.value,
                    )

        return application_metrics

    def run(
        self,
        metrics: List[t.ApplicationMetric],
        applications: Union[List[t.Application], List[str]],
        format: Enum = OutputFormat.OUTPUT_FORMAT_LOG,
    ) -> List[t.ApplicationMetric]:
        async def compute_metric(metric):
            metric.compute_and_set()
            if format == OutputFormat.OUTPUT_FORMAT_LOG:
                logging.info(
                    "%s/%s: %s",
                    metric.application.name,
                    metric.__class__.__name__,
                    metric.value,
                )

        async def async_run():
            if not isinstance(format, OutputFormat):
                raise TypeError(
                    f"Expected type to be `{type(OutputFormat)}`, got `{type(format)}`"
                )

            application_metrics = []
            tasks = []

            for application in applications:
                if isinstance(application, str):
                    application = t.Application(name=application)

                for Metric in metrics:
                    metric = Metric(application)  # type: ignore
                    application_metrics.append(metric)
                    tasks.append(compute_metric(metric))

            await asyncio.gather(*tasks)
            return application_metrics

        return asyncio.run(async_run())
