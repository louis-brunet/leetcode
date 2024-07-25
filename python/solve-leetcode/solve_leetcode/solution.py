from abc import abstractmethod
from typing import Generic, TypeVar


Input = TypeVar("Input")
Output = TypeVar("Output")


class Solution(Generic[Input, Output]):
    @abstractmethod
    def solve(self, input: Input) -> Output:
        pass

    def run_tests(self, test_cases: list[tuple[Input, Output]]) -> None: #list[tuple[bool, Output]]:
        for input, expected_output in test_cases:
            output = self.solve(input)

            if output != expected_output:
                print(f'[FAIL] Input: {input}; Output: {output}; Expected output: {expected_output}')
            else:
                print(f'[PASS] Input: {input}; Output: {output}')


class Solution0006(Solution[tuple[str, int], str]):
    def solve(self, input: tuple[str, int]) -> str:
        string_to_zigzag, num_rows = input

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
