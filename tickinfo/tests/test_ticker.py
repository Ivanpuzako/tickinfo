from ..tickinfo import Ticker
import pytest
import datetime
import pandas as pd
import matplotlib


@pytest.fixture()
def ticker():
    return Ticker("BTC-USD")


def test_get_info_type(ticker):
    time_hour = datetime.datetime(2021, 7, 10, 6)
    ret = ticker.info_last_hour(time_hour)
    assert isinstance(ret, pd.DataFrame)


def test_get_info_len(ticker):
    time_hour = datetime.datetime(2021, 7, 10, 6)
    ret = ticker.info_last_hour(time_hour)
    assert len(ret) == 12


def test_correct_average(ticker):
    hour_info = pd.DataFrame({
        "High": [4, 5, 6, 7],
        "Low": [3, 4, 5, 5]
    })
    idx = ['mean_price']
    expected = pd.DataFrame({
        "Low_mean": 4.25,
        "High_mean": 5.5
    }, index=['mean_price'])
    ret = ticker.calc_average(hour_info, index=idx)
    assert expected.equals(ret)


def test_sma(ticker):
    ret = ticker.calc_sma(datetime.datetime(2021, 7, 12, 5),
                          datetime.datetime(2021, 7, 12, 12),
                          window_size=1)
    assert len(ret) == 7


def test_fig(ticker):
    df = ticker.calc_sma(datetime.datetime(2021, 7, 12, 5),
                         datetime.datetime(2021, 7, 12, 12),
                         window_size=1)
    plot = ticker.create_date_plot({'data': df})
    assert issubclass(type(plot), matplotlib.axes.SubplotBase)
