import yfinance as yf
from backtesting import Backtest, Strategy
from backtesting.lib import crossover
from backtesting.test import SMA
import matplotlib.pyplot as plt

data = yf.download('GOOG', start='2020-01-01', end='2023-12-31')

class MySMAStrategy(Strategy):
    def init(self):
        price = self.data.Close
        self.ma1 = self.I(SMA, price, 10)
        self.ma2 = self.I(SMA, price, 20)

    def next(self):
        if crossover(self.ma1, self.ma2):
            self.buy()
        elif crossover(self.ma2, self.ma1):
            self.sell()

backtest = Backtest(data, MySMAStrategy, commission=0.002, exclusive_orders=True)
stats = backtest.run()
backtest.plot()
plt.show()
print(stats)