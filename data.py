from typing import List

from matplotlib import pyplot as plt
from yahoo_historical import Fetcher

from constants import PLOT_COLORS
from time_helper import time_from_today


def run():
    stocks = get_stocks()

    data = Fetcher(stocks[0], time_from_today(weeks=3)).get_historical()

    plot(data["Date"], data["Close"], data["Open"], color_index=1)

    plt.show()


def get_stocks() -> List:
    with open("companies.txt", "r") as f:
        data = f.readlines()
        data = [i.strip() for i in data]

        return data


def plot(dates, closes, opens, color_index=None):
    if color_index:
        plt.scatter(dates, closes, c=PLOT_COLORS[color_index])
    else:
        plt.scatter(dates, closes)


if __name__ == "__main__":
    run()
