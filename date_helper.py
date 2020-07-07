from datetime import date, timedelta
from typing import List


def one_month_from_today() -> List[int]:
    str_date = (date.today() - timedelta(days=30)).isoformat().split("-")
    return [int(value) for value in str_date]
