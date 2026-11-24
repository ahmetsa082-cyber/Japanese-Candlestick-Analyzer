
def detect_patterns(candles):
    patterns = []

    if len(candles) < 3:
        return patterns

    a = candles[-3]
    b = candles[-2]
    c = candles[-1]

    # Bullish Engulfing
    if (
        a.is_bearish
        and b.is_bullish
        and b.open <= a.close
        and b.close >= a.open
    ):
        patterns.append("Bullish Engulfing")

    # Bearish Engulfing
    if (
        a.is_bullish
        and b.is_bearish
        and b.open >= a.close
        and b.close <= a.open
    ):
        patterns.append("Bearish Engulfing")

    # Morning Star (simplified)
    if (
        a.is_bearish
        and b.body < a.body * 0.4
        and c.is_bullish
        and c.close > (a.open + a.close) / 2
    ):
        patterns.append("Morning Star")

    # Evening Star (simplified)
    if (
        a.is_bullish
        and b.body < a.body * 0.4
        and c.is_bearish
        and c.close < (a.open + a.close) / 2
    ):
        patterns.append("Evening Star")

    return patterns
