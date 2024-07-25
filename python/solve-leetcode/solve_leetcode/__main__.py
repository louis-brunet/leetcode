from typing import TypeVar
from solution import Solution0006


Input = TypeVar("Input")
Output = TypeVar("Output")


# def run_tests(solutions: list[tuple[Solution[Input, Output], list[tuple[Input, Output]]]]):
#     for solution, test_cases in solutions:
#         results = solution.run_tests(test_cases)
#
#         for index, result in enumerate(results):
#             if not result:
#                 (failed_input = test_cases[index]
#                 print(f'[FAIL] Test case: {failed_test_case}')


def main():
    s = Solution0006()
    s.run_tests(
        [
            (("PAYPALISHIRING", 3), "PAHNAPLSIIGYIR"),
            (("PAYPALISHIRING", 4), "PINALSIGYAHRPI"),
            (("A", 1), "A"),
            (("ABC", 1), "ABC"),
        ]
    )

    # raise Exception("TODO")


if __name__ == "__main__":
    main()
