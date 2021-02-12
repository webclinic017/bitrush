from decimal import *
from lib.strategies.base_strategy import StrategyParams
from lib.strategies.volatility_breakout import VolatilityBreakout
from lib.strategies.stoch_rsi import StochRSI
from lib.strategies.golden_cross import GoldenCross
from lib.strategies.aroon import Aroon
from lib.strategies.rsi_bb import RsiBB
from lib.ticker import Ticker
from lib.broker import Broker
from lib.upbit import Upbit
import json
from lib.sqs import order_queue

api = Upbit()
broker = Broker(api, order_queue)


def test_get_order():
    sell_order = api.get_order("fbd50fdf-9f6c-4d11-98f7-554cca2dc946")
    buy_order = api.get_order("714e432e-8ccb-4d90-bc31-d00644da47a6")
    print(json.dumps(sell_order, indent=2))
    print(json.dumps(buy_order, indent=2))


def test_notify_order():
    broker.notify_order(
        order_id="714e432e-8ccb-4d90-bc31-d00644da47a6",
        type="buy",
        ticker="BTC",
        price=Decimal("41351000.00000000"),
        size=Decimal("0.00018350"),
    )


def test_volatility_breakout():
    strategy = VolatilityBreakout(
        broker,
        StrategyParams(ticker=Ticker.비트코인.value, ratio=Decimal(0.2)),
    )
    strategy.should_buy()
    strategy.should_sell()


def test_stoch_rsi():
    strategy = StochRSI(
        broker, StrategyParams(ticker=Ticker.비트코인.value, ratio=Decimal(0.2))
    )
    strategy.should_buy()
    strategy.should_sell()


def test_golden_cross():
    strategy = GoldenCross(
        broker, StrategyParams(ticker=Ticker.비트코인.value, ratio=Decimal(0.2))
    )
    strategy.should_buy()
    strategy.should_sell()


def test_aroon():
    strategy = Aroon(
        broker, StrategyParams(ticker=Ticker.비트코인.value, ratio=Decimal(0.2))
    )
    strategy.should_buy()
    strategy.should_sell()


def test_rsi_bb():
    strategy = RsiBB(
        broker, StrategyParams(ticker=Ticker.비트코인.value, ratio=Decimal(0.2))
    )
    strategy.should_buy()
    strategy.should_sell()


def test_get_orders():
    res = api.get_orders(ticker=Ticker.이더리움.value, state="cancel")
    print(res)