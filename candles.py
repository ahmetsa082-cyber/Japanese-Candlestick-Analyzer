
class Candle:
    def __init__(self, open_price, high, low, close):
        self.open = float(open_price)
        self.high = float(high)
        self.low = float(low)
        self.close = float(close)

        self.body = abs(self.close - self.open)

        self.upper_wick = (
            self.high - max(self.open, self.close)
        )

        self.lower_wick = (
            min(self.open, self.close) - self.low
        )

        self.is_bullish = self.close > self.open
        self.is_bearish = self.close < self.open
        self.is_doji = self.close == self.open

    def get_shape(self):
        if self.is_doji:
            return "Doji"

        if self.upper_wick > self.body * 2 and self.lower_wick < self.body:
            return "Shooting Star"

        if self.lower_wick > self.body * 2 and self.upper_wick < self.body:
            return "Hammer"

        if self.body > 0 and self.upper_wick < self.body * 0.1 and self.lower_wick < self.body * 0.1:
            return "Marubozu"

        return "Normal Candle"

    def get_direction(self):
        if self.is_bullish:
            return "Bullish"

        if self.is_bearish:
            return "Bearish"

        return "Neutral"
