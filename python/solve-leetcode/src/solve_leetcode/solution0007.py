from solution import Solution

INT_MIN = -(1 << 31)
INT_MAX = (1 << 31) - 1


class Solution0007(Solution[int, int]):
    def __init__(self) -> None:
        super().__init__(
            [
                (123, 321),
                (-123, -321),
                (120, 21),
                (0, 0),
                (1, 1),
                (-1, -1),
                ((1 << 31) + 9, 0),
            ]
        )

    def solve(self, input: int) -> int:
        reversed = 0
        is_negative = input < 0

        input = abs(input)
        while input != 0:
            input_unit = input % 10
            input = int(input / 10)

            if reversed < INT_MIN + input_unit + reversed * 9 or reversed > INT_MAX - reversed * 9 - input_unit:
                return 0
            reversed = reversed * 10 + input_unit

        # if reversed < INT_MIN or reversed > INT_MAX:
        #     return 0

        if is_negative:
            return -reversed

        return reversed
