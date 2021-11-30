from typing import List


class Quote:
    volume: List[int]
    open: List[float]
    high: List[float]
    close: List[float]
    low: List[float]

    def __init__(self, volume: List[int], open: List[float], high: List[float], close: List[float], low: List[float]) -> None:
        self.volume = volume
        self.open = open
        self.high = high
        self.close = close
        self.low = low


class Indicators:
    quote: List[Quote]

    def __init__(self, quote: List[Quote]) -> None:
        self.quote = quote


class Post:
    timezone: str
    start: int
    end: int
    gmtoffset: int

    def __init__(self, timezone: str, start: int, end: int, gmtoffset: int) -> None:
        self.timezone = timezone
        self.start = start
        self.end = end
        self.gmtoffset = gmtoffset


class CurrentTradingPeriod:
    pre: Post
    regular: Post
    post: Post

    def __init__(self, pre: Post, regular: Post, post: Post) -> None:
        self.pre = pre
        self.regular = regular
        self.post = post


class Meta:
    currency: str
    symbol: str
    exchange_name: str
    instrument_type: str
    first_trade_date: int
    regular_market_time: int
    gmtoffset: int
    timezone: str
    exchange_timezone_name: str
    regular_market_price: float
    chart_previous_close: float
    previous_close: float
    scale: int
    price_hint: int
    current_trading_period: CurrentTradingPeriod
    trading_periods: List[List[Post]]
    data_granularity: str
    range: str
    valid_ranges: List[str]

    def __init__(self, currency: str, symbol: str, exchange_name: str, instrument_type: str, first_trade_date: int, regular_market_time: int, gmtoffset: int, timezone: str, exchange_timezone_name: str, regular_market_price: float, chart_previous_close: float, previous_close: float, scale: int, price_hint: int, current_trading_period: CurrentTradingPeriod, trading_periods: List[List[Post]], data_granularity: str, range: str, valid_ranges: List[str]) -> None:
        self.currency = currency
        self.symbol = symbol
        self.exchange_name = exchange_name
        self.instrument_type = instrument_type
        self.first_trade_date = first_trade_date
        self.regular_market_time = regular_market_time
        self.gmtoffset = gmtoffset
        self.timezone = timezone
        self.exchange_timezone_name = exchange_timezone_name
        self.regular_market_price = regular_market_price
        self.chart_previous_close = chart_previous_close
        self.previous_close = previous_close
        self.scale = scale
        self.price_hint = price_hint
        self.current_trading_period = current_trading_period
        self.trading_periods = trading_periods
        self.data_granularity = data_granularity
        self.range = range
        self.valid_ranges = valid_ranges


class Result:
    meta: Meta
    timestamp: List[int]
    indicators: Indicators

    def __init__(self, meta: Meta, timestamp: List[int], indicators: Indicators) -> None:
        self.meta = meta
        self.timestamp = timestamp
        self.indicators = indicators


class Chart:
    result: List[Result]
    error: None

    def __init__(self, result: List[Result], error: None) -> None:
        self.result = result
        self.error = error


class ActionModel:
    chart: Chart

    def __init__(self, chart: Chart) -> None:
        self.chart = chart
