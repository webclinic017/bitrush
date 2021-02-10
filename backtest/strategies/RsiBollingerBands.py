from backtrader import bt
from backtest.indicators.StochRSI import StochRSI


class RsiBollingerBands(bt.Strategy):
    params = (
        ("ratio", 0.2),
        ("min_trade", 5000),
    )

    def __init__(self) -> None:
        super().__init__()
        self.bb = bt.indicators.BollingerBands(self.data, period=14)
        self.rsi = StochRSI(self.data, period=14)
        self.bb_crossup = bt.indicators.CrossUp(self.data.close, self.bb.top)
        self.bb_crossdown = bt.indicators.CrossDown(self.data.close, self.bb.bot)

    def next(self):
        cash = self.broker.get_cash()
        position = self.getposition()

        if not position and self.rsi[0] >= 0.8 and self.bb_crossup[0] == 1:
            if cash * self.p.ratio > self.p.min_trade:
                self.order_target_percent(target=self.p.ratio)
        elif position and self.rsi[0] <= 0.3:
            self.close()
