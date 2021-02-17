from lib.strategies.base_strategy import BaseStrategy
from talib import abstract, MA_Type


class DcBreakout(BaseStrategy):
    name = "dc_breakout"

    # settings
    low_period = 2
    high_period = 4

    def __init__(self, broker, params) -> None:
        super().__init__(broker, params)
        ticker = self.params["ticker"]

        feed = self.broker.get_feed(ticker)

        dch = abstract.MAX(feed["close"], timeperiod=self.high_period)
        dcl = abstract.MIN(feed["close"], timeperiod=self.low_period)

        feed["dch"] = dch
        feed["dcl"] = dcl
        prev_close = feed["close"].shift(1)
        prev_dch = feed["dch"].shift(1)
        prev_dcl = feed["dcl"].shift(1)

        feed["cross_up"] = (feed["close"] >= feed["dch"]) & (prev_close < prev_dch)
        feed["cross_down"] = (feed["close"] <= feed["dcl"]) & (prev_close > prev_dcl)

        self.current_ohlcv = feed.iloc[-1]

    def should_buy(self) -> bool:
        return self.current_ohlcv["cross_up"]

    def should_sell(self) -> bool:
        return self.current_ohlcv["cross_down"]
