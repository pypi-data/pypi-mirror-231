from datetime import datetime, timedelta

import pytest

from dateweek import DateWeek

base_year = 2023
base_week = 32
base_date_first_day = datetime(2023, 8, 6)
base_date_last_day = base_date_first_day + timedelta(days=7)


def test_dateweek():
    dateweek = DateWeek(week=base_week, year=base_year)
    assert dateweek


def test_dateweek_dt():
    dateweek = DateWeek(week=base_week, year=base_year)
    assert dateweek._dt == base_date_first_day


def test_first_day():
    dateweek = DateWeek(week=base_week, year=base_year)
    assert dateweek.first_day == base_date_first_day


def test_last_day():
    dateweek = DateWeek(week=base_week, year=base_year)
    assert dateweek.last_day == base_date_last_day


def test_ts_list():
    raise NotImplementedError


def test_add():
    dateweek = DateWeek(week=base_week, year=base_year)
    dateweek_add = dateweek + 1
    assert dateweek_add.week == base_week + 1
    assert dateweek_add.year == base_year
    # Most years have 52 weeks; this test uses this knowledge to test the addition between years.
    dateweek_add_year = dateweek + 52
    assert dateweek_add_year.year == base_year + 1


def test_sub():
    dateweek = DateWeek(week=base_week, year=base_year)
    dateweek_sub = dateweek - 1
    assert dateweek_sub.week == base_week - 1
    assert dateweek_sub.year == base_year
    # Most years have 52 weeks; this test uses this knowledge to test the subtraction between years.
    dateweek_sub_year = dateweek - 52
    assert dateweek_sub_year.year == base_year - 1


def test_current_week():
    dateweek = DateWeek.current_week()
    dt = datetime.now()
    year = int(dt.strftime("%Y"))
    week = int(dt.strftime("%U"))
    assert dateweek.week == week
    assert dateweek.year == year


def test_from_datetime():
    dateweek = DateWeek.from_datetime(base_date_first_day)
    assert dateweek.year == base_year
    assert dateweek.week == base_week
    assert dateweek._dt == base_date_first_day
    assert dateweek.first_day == base_date_first_day
    assert dateweek.last_day == base_date_last_day


def test_from_str():
    dateweek = DateWeek.from_str("2023-08-06")
    assert dateweek
    assert dateweek.week == base_week
    assert dateweek.year == base_year


def test_week_date_range():
    dateweek = DateWeek(week=base_week, year=base_year)
    assert dateweek.date_range() == (base_date_first_day, base_date_last_day)
    assert dateweek.date_range(as_string=True) == (
        base_date_first_day.strftime("%Y-%m-%d %H:%M:%S"),
        base_date_last_day.strftime("%Y-%m-%d %H:%M:%S"),
    )


def test_week_0_coercion():
    with pytest.raises(ValueError):
        DateWeek(week=0, year=2021)

    # Given that, in 2023 week 0 and 2023 week 1 are the same
    # 2023 week 0 should be coerced to 2023 week 1 because
    # WEEK 0 DOES NOT ACTUALLY EXIST IN THIS CASE (because there is no overflow from the previous year)
    dt = datetime(2023, 1, 1)
    dateweek = DateWeek.from_datetime(dt)
    assert dateweek.week == 1

    # !!! PLEASE !!! =====> READ THE COMMENT ABOVE <===== !!! PLEASE !!!
    # Given that there is overflow from the previous year
    # 2021 week 0 should be coerced to 2020 week 52
    dt = datetime(2021, 1, 1)
    dateweek = DateWeek.from_datetime(dt)
    # 2021 IS NOT a long year, so it has 52 weeks
    assert dateweek.week == 52


def test_change_year_week():
    dateweek = DateWeek(year=base_year, week=base_week)
    with pytest.raises(ValueError):
        dateweek.week = 1

    with pytest.raises(ValueError):
        dateweek.year = 2021
