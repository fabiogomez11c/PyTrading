from backtester.events import MarketEvent, SignalEvent
from queue import Queue
from collections import namedtuple

import numpy as np


class MAcross:

    def __init__(self, events: Queue, parameters: namedtuple) -> None:
        """
        Strategy instance that follows a moving average crossover.
        """

        self.events = events
        self.parameters = parameters

    def compute_signal(self, event: MarketEvent) -> None:
        """
        Computes the indicators and the signal according to the market data.
        """
        pass
