from dataclasses import dataclass
from datetime import datetime, timedelta
from functools import cached_property
from typing import List, Optional, Tuple, Union

WEEK_FORMAT = "%Y-%U-%w"
DATE_FORMAT = "%Y-%m-%d"
DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"


@dataclass
class DateWeek:
    def __init__(self, year: int, week: int, coerce_week: bool = False):
        """Container class for "w-sat" weeks.

        Args:
            year (int): Year
            week (int): Number of the week
            coerce_week (bool, optional):
                Defines if week 0 is allowed. If so, it will be coerced to the last week of the
                previous year.
                    Defaults to False.

        Raises:
            ValueError: Will raise a ValueError if week is set to 0 but 0 is not allowed.
        """
        if week == 0 and not coerce_week:
            raise ValueError("Week 0 is not a valid week")

        dt = datetime.strptime(f"{year}-{week}-0", WEEK_FORMAT)

        if int(dt.strftime("%U")) == 0:
            year = int(dt.strftime("%Y")) - 1
            week = int(dt.strptime(f"{year}-12-31", DATE_FORMAT).strftime("%U"))

        self._dt = dt
        self._year = year
        self._week = week

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(year={self.year}, week={self.week})"

    @property
    def week(self) -> int:
        return self._week

    @property
    def year(self) -> int:
        return self._year

    @week.setter
    def week(self, _: any):
        raise ValueError("Week is a read-only property")

    @year.setter
    def year(self, _: any):
        raise ValueError("Year is a read-only property")

    @property
    def first_day(self) -> datetime:
        return self._dt

    @cached_property
    def last_day(self) -> datetime:
        return self._dt + timedelta(days=7)

    @cached_property
    def ts_list(self) -> List[datetime]:
        return [self.first_day + timedelta(minutes=10 * i) for i in range(144 * 7)]

    def __add__(self, other: int) -> "DateWeek":
        if not isinstance(other, int):
            raise ValueError("Only integers can be added to DateWeek")
        new_dt = self._dt + timedelta(days=other * 7)
        return self.from_datetime(new_dt)

    def __sub__(self, other: int) -> "DateWeek":
        if not isinstance(other, int):
            raise ValueError("Only integers can subtract from DateWeek")
        new_dt = self._dt - timedelta(days=other * 7)
        return self.from_datetime(new_dt)

    @classmethod
    def current_week(cls) -> "DateWeek":
        return cls.from_datetime(datetime.now())

    @staticmethod
    def from_datetime(dt: datetime) -> "DateWeek":
        if (week := int(dt.strftime("%U"))) == 0:
            year = int(dt.strftime("%Y")) - 1
            week = int(dt.strptime(f"{year}-12-31", DATE_FORMAT).strftime("%U"))
            return DateWeek(year=year, week=week, coerce_week=True)
        return DateWeek(year=int(dt.strftime("%Y")), week=week, coerce_week=True)

    @classmethod
    def from_str(cls, date_str: str, date_format: str = DATE_FORMAT) -> "DateWeek":
        return cls.from_datetime(datetime.strptime(date_str, date_format))

    def date_range(
        self, as_string: Optional[bool] = False
    ) -> Union[Tuple[datetime, datetime], Tuple[str, str]]:
        if as_string:
            return self.first_day.strftime(DATETIME_FORMAT), self.last_day.strftime(DATETIME_FORMAT)
        return self.first_day, self.last_day
