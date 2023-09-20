# J formatter Logger Converter

The J formatter is a Python package that allows users to convert time in seconds to the Jira time logger format. This package can be used if your project want such a timer logger setup which is able to represent the time in a particular format

## Installation

You can install the package using pip:

```bash
pip install j_formatter

from j_formatter import convert_to_j_format

# Example usage:
time_in_seconds = 45000  # Replace with your desired time in seconds
jira_time_format = convert_to_j_format(time_in_seconds)
print(jira_time_format)
