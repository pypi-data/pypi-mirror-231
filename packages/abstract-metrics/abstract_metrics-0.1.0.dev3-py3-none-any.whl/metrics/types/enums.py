from enum import Enum, auto


class OutputFormat(Enum):
    """Defines the output formats for metrics generation."""

    OUTPUT_FORMAT_UNSPECIFIED = auto()
    OUTPUT_FORMAT_LOG = auto()
    OUTPUT_FORMAT_MARKDOWN = auto()
    OUTPUT_FORMAT_JSON = auto()
    OUTPUT_FORMAT_YAML = auto()
