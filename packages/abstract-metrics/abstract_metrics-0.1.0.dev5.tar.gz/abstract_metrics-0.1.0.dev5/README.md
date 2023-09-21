[![Check All](https://github.com/Fraser-Isbester/metric/actions/workflows/check.yaml/badge.svg)](https://github.com/Fraser-Isbester/metric/actions/workflows/check.yaml) [![Build & Publish](https://github.com/Fraser-Isbester/metric/actions/workflows/build-and-publish.yaml/badge.svg)](https://github.com/Fraser-Isbester/metric/actions/workflows/build-and-publish.yaml)

# ✨Abstract✨ metrics
A lightweight framework for defining arbitrary business metrics as Python code.

# Installation
```bash
pip install abstract-metrics
```

# Basic Usage

1. Install
2. Subclass one of the metric types (e.g. ApplicationMetricBoolean)
3. Add an optimistic `compute` method that returns your metric.
4. Register a runner with your metric and run it!

# Example
Let's say you want to write a metric that checks if one of your applications follows your organizations application naming standards. We will use the ApplicationMetricBoolean type to do this. All metrics are formated as `{subject}Metric{type}`. In this case, our subject is an `Application` and our type is `Boolean`.

Because Applications are our subject, we need to subclass `ApplicationMetricBoolean`. This class has a few methods that we can use to help us compute our metric. The most important one is `compute`. This method is called by the runner and should return a the boolean value. Additionally, we should use the `application` property (via the `Application` wrapper) to store any context we need to compute this metric.

```python

from metric import Application, ApplicationMetric
from metric.utils import MatrixRunner
from metric.types import OutputFormat

def main():
    # Construct list of basic Application objects
    apps = [Application(app) for app in ["myorg-sales-app", "sandbox-dinasour"]]
    # Construct a list of our metrics
    metrics = [AppNameCompliance]

    # This will not only construct our Application Metrics but it will also execute
    # them and print them to stdout as a table.
    MatrixRunner(format=OutputFormat.OUTPUT_FORMAT_TABLE).run(apps, metrics)

class AppNameCompliance(ApplicationMetricBoolean):
    r"""All Application names should start with 'myorg-'."""

    def compute(self):
        if self.application.name.startswith("myorg-"):
            return True
        return False
```

If we run this code, we'll get the following output:

```bash
Application             AppNameCompliance
myorg-finance-app                    True
myorg-marketing-service              True
myorg-sales-app                      True
sandbox-dinasour                    False
```
