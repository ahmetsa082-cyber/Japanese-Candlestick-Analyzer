
from candles import Candle
from patterns import detect_patterns


def analyze_candles(candles):
    print("\n===== تحليل الشموع اليابانية =====\n")

    for i, candle in enumerate(candles, 1):
        print(f"الشمعة {i}")
        print("الشكل:", candle.get_shape())
        print("الاتجاه:", candle.get_direction())
        print("الجسم:", candle.body)
        print("الظل العلوي:", candle.upper_wick)
        print("الظل السفلي:", candle.lower_wick)
        print("--------------------")

    patterns = detect_patterns(candles)

    print("\nالأنماط المكتشفة:")

    if patterns:
        for pattern in patterns:
            print("-", pattern)
    else:
        print("لم يتم اكتشاف نمط واضح.")


candles = [
    Candle(110, 112, 105, 106),
    Candle(106, 108, 104, 107),
    Candle(105, 113, 104, 112),
]

analyze_candles(candles)
