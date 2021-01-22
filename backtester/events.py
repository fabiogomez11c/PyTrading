"""
Events classes to handle into the Queue.
"""

from typing import Dict

class MarketEvent:

    def __init__(self):
        """
        Market event.
        """
        self.event = 'Market'

class SignalEvent:

    def __init__(self, info: Dict) -> None:
        """
        Signal event, contains information about the signal to be transmitted.
        """
        self.event = 'Signal'
        self.info = info

class OrderEvent:

    def __init__(self, info: Dict) -> None:
        """
        Order event, contains information to execute the order in the market.
        """
        self.event = 'Order'
        self.info = info

class FillEvent:

    def __init__(self, info: Dict) -> None:
        """
        Fill event, contains the information needed to keep the portfolio updated.
        """
        self.event = 'Fill'
        self.info = info
