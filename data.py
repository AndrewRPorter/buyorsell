from matplotlib import pyplot as plt
from yahoo_historical import Fetcher

from date_helper import one_month_from_today


def run():
    data = Fetcher("AAPL", one_month_from_today()).get_historical()

    closes = data["Close"]
    opens = data["Open"]
    dates = data["Date"]

    plot(dates, closes, opens)


def plot(dates, closes, opens):
    plt.scatter(dates, closes, c="r")
    plt.scatter(dates, opens, c="g")
    plt.show()


if __name__ == "__main__":
    run()
