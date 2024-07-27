from solution import Solution


class Solution0006(Solution[tuple[str, int], str]):
    def __init__(self) -> None:
        super().__init__([
            (("PAYPALISHIRING", 3), "PAHNAPLSIIGYIR"),
            (("PAYPALISHIRING", 4), "PINALSIGYAHRPI"),
            (("A", 1), "A"),
            (("ABC", 1), "ABC"),
        ])

    def solve(self, input: tuple[str, int]) -> str:
        string_to_zigzag, num_rows = input
        if num_rows == 1:
            return string_to_zigzag

        rows = ["" for _ in range(num_rows)]
        current_row = 0
        moving_down = True

        for char in string_to_zigzag:
            rows[current_row] += char

            if current_row == num_rows - 1:
                moving_down = False
                if current_row != 0:
                    current_row -= 1
            elif moving_down:
                current_row += 1
            elif current_row == 0:
                moving_down = True
                current_row += 1
            else:
                current_row -= 1

        return "".join(rows)

