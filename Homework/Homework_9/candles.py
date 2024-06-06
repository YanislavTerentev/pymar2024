"""This program return candles number"""


def solution(candles_number, make_new):
    """This program return candles number"""
    result = candles_number
    candle_remnants = candles_number
    while candle_remnants >= make_new:
        new_candles_number = candle_remnants // make_new
        result += new_candles_number
        candle_remnants = new_candles_number + (candle_remnants % make_new)
    return result


assert solution(5, 2) == 9, "Your answer should be 9"
assert solution(1, 2) == 1, "Your answer should be 1"
assert solution(15, 5) == 18, "Your answer should be 18"
assert solution(12, 2) == 23, "Your answer should be 23"
assert solution(6, 4) == 7, "Your answer should be 7"
assert solution(13, 5) == 16, "Your answer should be 16"
assert solution(2, 3) == 2, "Your answer should be 2"
