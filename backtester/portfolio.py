from backtester.events import SignalEvent, OrderEvent, FillEvent, MarketEvent

from queue import Queue

class Portfolio:

    def __init__(self) -> None:
        """
        Instance that contains all the computations related to the portfolio handling
        """
        pass

    def update_from_signal(self, event: SignalEvent) -> None:
        """
        Update the portfolio from the signal event, basically it creates an order based on
        the information from the signal event.
        """
        pass

    def update_from_order(self, event: OrderEvent) -> None:
        """
        Update the portfolio from the order event, basically it creates a fill event based
        on the information contained in the OrderEvent.
        """
        pass

    def update_from_fill(self, event: FillEvent) -> None:
        """
        Update the porftolio from the fill event, basically it store and compute the 
        information related to the trades, profit or loss, useful information, etc...
        """
        pass
    
    def update_from_market(self, event: MarketEvent) -> None:
        """
        Update the portfolio from the market event, basically it stores information
        that needs to be obtained each candle.
        """
        pass
