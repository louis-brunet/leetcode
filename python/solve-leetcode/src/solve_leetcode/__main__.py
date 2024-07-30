from typing import TypeVar
from solution0006 import Solution0006
from solution0007 import Solution0007
from solution0010 import Solution0010
from solution0010naive import Solution0010Naive


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
    solutions = [
        Solution0006(),
        Solution0007(),
        # Solution0010Naive(),
        Solution0010(),
    ]
    for solution in solutions:
        solution.run_tests()
        print()


if __name__ == "__main__":
    main()
