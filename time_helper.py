from datetime import date, timedelta
from typing import List


def time_from_today(months=0, weeks=0) -> List[int]:
    days = (7 * weeks) + (30 * months)

    str_date = (date.today() - timedelta(days=days)).isoformat().split("-")
    return [int(value) for value in str_date]
