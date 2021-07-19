tickinfo
--------

To import and run Ticker module do::

    >>> from tickinfo import Ticker
    >>> ticker_name = "AAPL"
    >>> ticker = Ticker(ticker_name)
 rebuild:
 ```
 python setup.py bdist_wheel

 twine upload --skip-existing dist/*
 ```