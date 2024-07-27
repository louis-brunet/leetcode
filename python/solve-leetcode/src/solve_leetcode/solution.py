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
            output = self.solve(input)

            if output != expected_output:
                print(
                    f"[FAIL] {self.__class__.__name__} -- Input: {input}; Output: {output}; Expected output: {expected_output}"
                )
            else:
                print(f"[PASS] {self.__class__.__name__} -- Input: {input}; Output: {output}")
