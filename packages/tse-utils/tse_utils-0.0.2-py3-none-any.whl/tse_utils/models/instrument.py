from dataclasses import dataclass
from tse_utils.models.enums import Nsc
from tse_utils.models.realtime import *
from datetime import time, date, datetime

@dataclass
class InstrumentIdentification:
    """
    Holds the identification for instruments.
    """
    id: int = None
    isin: str = None
    tsetmc_code: str = None
    ticker: str = None
    name_persian: str = None
    name_english: str = None

    def __str__(self):
        return f"{self.ticker} [{self.isin}]"
    
class Instrument:
    """
    Holds all available data for a specific tradable instrument.
    """
    def __init__(self, identification: InstrumentIdentification, max_price_threshold: int = None, min_price_threshold: int = None, 
                 max_buy_order_quantity_threshold: int = None, max_sell_order_quantity_threshold: int = None, base_volume: int = 1, 
                 lot_size: int = 1, total_shares: int = None, price_tick: int = 1, is_obsolete: bool = False, nsc: Nsc = None):
        self.identification = identification
        self.max_price_threshold = max_price_threshold
        self.min_price_threshold = min_price_threshold
        self.max_buy_order_quantity_threshold = max_buy_order_quantity_threshold
        self.max_sell_order_quantity_threshold = max_sell_order_quantity_threshold
        self.base_volume = base_volume
        self.lot_size = lot_size
        self.total_shares = total_shares
        self.price_tick = price_tick
        self.is_obsolete = is_obsolete
        self.nsc = nsc
        self.orderbook = OrderBook()
        self.client_type = ClientType()
        self.intraday_trade_candle = TradeCandle()
        self.deep_orderbook = DeepOrderBook()

    def ticker_with_tsetmc_hyperlink(self) -> str:
        """
        Returns an HTML element containing a hyperlink to the TSETMC page for instrument.
        """
        return f"<a href=\"http://www.tsetmc.com/Loader.aspx?ParTree=151311&i={self.identification.tsetmc_code}\">{self.identification.ticker}</a>"

    def has_buy_queue(self) -> bool:
        return self.orderbook.rows[0].demand_price == self.max_price_threshold

    def has_sell_queue(self) -> bool:
        return self.orderbook.rows[0].supply_price == self.min_price_threshold

    def __str__(self):
        return str(self.identification)

class DerivativeInstrument(Instrument):
    '''
    Derivative instrument contains a self.underlying that represents the underlying instrument.
    '''
    def __init__(self, underlying: Instrument, **kwargs):
        self.underlying = underlying
        super().__init__(**kwargs)

class OptionInstrument(DerivativeInstrument):

    def __init__(self, exercise_date: date, exercise_price: int, lot_size: int = None, **kwargs):
        self.exercise_date = exercise_date
        self.exercise_price = exercise_price
        self.lot_size = lot_size
        super().__init__(**kwargs)

@dataclass
class IndexIdentification:
    """
    Holds the identification for an index, for example the overal index.
    """
    tsetmc_code: str = None
    persian_name:str = None

    def __str__(self) -> str:
        return f"{self.persian_name} [{self.tsetmc_code}]"

class Index:
    """
    Holds all available data for a specific index.
    """
    def __init__(self, identification: IndexIdentification, min_value: int = None, max_value: int = None,
                 last_value: int = None):
        self.identification = identification
        self.min_value = min_value
        self.max_value = max_value
        self.last_value = last_value

    def __str__(self) -> str:
        return f"{self.identification}"

