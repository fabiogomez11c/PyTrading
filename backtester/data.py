"""
The FXCM documentation: https://www.fxcm.com/fxcmpy/?fx_sh=ZnhjbW1hcmtldHM=&fx_lce&fx_sid&cmp&btag
"""

import json
import fxcmpy

from queue import Queue
from backtester.events import MarketEvent

def get_token():
    """
    Get the token from the config.json file.
    """
    with open("config.json") as f:
        config_data = json.load(f)
    
    return config_data['TOKEN']

class FXCMHistoricalData:

    def __init__(self, events: Queue):
        self.token = get_token()
        self.historical_bars = []
        self.events = events

        # get the historical data
        self._get_data('EUR/USD')
    
    def _get_data(self, instrument: str):
        """
        Get data from the FXCM server
        """

        # Creates the connection
        con = fxcmpy.fxcmpy(
            access_token=self.token,
            log_level='error',
            server='demo',  # 'real' for live trading
            log_file='log.txt'
        )

        # check if connection is good
        if not con.is_connected():
            print('Connection Failed')
            exit()
        
        # Fetching the data from FXCM
        data = con.get_candles(instrument, period='H1', number=200, columns=['bids'])

        # Convert data into a iterable
        # Remember OCHL (not OHLC)
        self.data = data.iterrows()
        self._convert_data()

    def _convert_data(self):
        """
        Converts the data into an iterable to memory efficient.
        """
        for market_data in self.data:
            yield (
                market_data[0],  # timestamp
                market_data[1][0],  # open
                market_data[1][1],  # close
                market_data[1][2],  # high
                market_data[1][3]  # low
            )

    def update_bars(self):
        """
        Updates the historical available data.
        """
        bars = next(self._convert_data())
        self.historical_bars.append(bars)
        self.events.put(MarketEvent())

    def get_latest_bars(self, N=1):
        """
        Get the latest bars given a N.
        """
        return self.historical_bars[-N]
