import yfinance as yf
import finta as ft
from backtesting import Backtest, Strategy
from backtesting.lib import crossover
import matplotlib.pyplot as plt

class MyMACDStrategy(Strategy):
    def init(self):
        price = self.data.Close
        self.macd = self.I(lambda X: talib.MACD(X)[0], price)
        self.macd_signal = self.I(lambda x: talib.MACD(x)[1], price)

    def next(self):
        if crossover(self.macd, self.macd_signal):
            self.buy()
        elif crossover(self.macd_signal, self.macd):
            self.sell()

start = '2020-01-01'
end = '2023-01-01'
data = yf.download("TSLA", start=start, end=end)

backtest = Backtest(data, MyMACDStrategy, commission=0.002, exclusive_orders=True)
stats = backtest.run()
print(stats)
backtest.plot()
plt.show()