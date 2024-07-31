from abc import ABC, abstractmethod
from typing import Generic, TypeVar


Input = TypeVar("Input")
Output = TypeVar("Output")


class Solution(ABC, Generic[Input, Output]):
    def __init__(self, test_cases: list[tuple[Input, Output]]) -> None:
        super().__init__()
        self.test_cases = test_cases

    @abstractmethod
    def solve(self, input: Input) -> Output:
        pass

    def run_tests(self) -> None:
        for input, expected_output in self.test_cases:
            input_str = str(input)
            output = self.solve(input)

            if output != expected_output:
                print(
                    f"[\033[31mFAIL\033[0m] {self.__class__.__name__} -- Input: {input_str}; Output: {output}; Expected output: {expected_output}"
                )
            else:
                print(f"[\033[32mPASS\033[0m] {self.__class__.__name__} -- Input: {input_str}; Output: {output}")
