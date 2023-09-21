# DateWeek

DateWeek is a Python package for working with w-sat weeks.

## Usage

```python
from dateweek import DateWeek
from datetime import datetime

# Creating a DateWeek object for the current week
current_week = DateWeek.current_week()

# Creating a DateWeek object for a specific week
week = DateWeek(2020, 1)

# Creating a DateWeek object from a datetime
week = DateWeek.from_datetime(datetime(2020, 1, 1))


# Creating a DateWeek object from a string
week = DateWeek.from_str("2020-01-01")

# Getting the first day and last day of the week
first_day, last_day = week.first_day, week.last_day


# Finding the previous week
previous_week = current_week - 1

# Finding the next week
next_week = current_week + 1

```

## Development

### Conda

```bash
conda env create -f environment.yml
conda activate dateweek
pip install -e .
pip install -e .[dev]
pip install -e .[unittest]
```
