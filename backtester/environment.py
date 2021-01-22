# import all the custom packages
from backtester.data import FXCMHistoricalData
from backtester.analyzer import Coach
from backtester.portfolio import Portfolio
from backtester.strategy import MAcross

from queue import Queue
from collections import namedtuple
from multiprocessing import Pool
import datetime

class Environment:

    def __init__(self, from_date: str, to_date: str, symbol: str,
        strategy_params: namedtuple):
        
        self.from_date = from_date
        self.to_date = to_date
        self.symbol = symbol
        self.strategy_params = strategy_params

        # get the correct start and end dates
        self._divide_by_year()

    def run(self):
        """
        Run several backtests at the same time.
        """

    def run_backtest(self, start_date: datetime.datetime, end_date: datetime.datetime):
        """
        Run an individual backtest given a start date and end date
        """

        # elements of the backtesting
        events = Queue()
        strategy = MAcross(events, self.strategy_params)
        portfolio = Portfolio()
        data = FXCMHistoricalData(events)
        coach = Coach()  # this instance will help to improve the strategy

    def _divide_by_year(self):
        """
        Take the user input (from_date and to_date) and divide it per year, 
        so the multiprocessing will be executing it, one core one year.
        """
        
        # clean the user input
        from_ = datetime.datetime.strptime(self.from_date, format="%Y-%m-%D")
        to_ = datetime.datetime.strptime(self.to_date, format="%Y-%m-%D")

        # recursive functions to get the correct froms and tos
        def from_rec(start_date: datetime.datetime):
            new_date = datetime.datetime(start_date.year + 1, 1, 1)
            if new_date > to_:
                return []
            else:
                return [new_date] + from_rec(new_date)
        
        def to_rec(end_date: datetime.datetime):
            new_date = datetime.datetime(end_date.year - 1, 12, 31)
            if new_date < from_:
                return []
            else:
                return [new_date] + from_rec(new_date)

        # get the list with the star and end of each process
        from_list = [from_] + from_rec(from_)
        to_list = [to_] + from_rec(to_)
        to_list = to_list[::-1]

        # this attribute is an iterator
        self.correct_dates = zip(from_list, to_list)
