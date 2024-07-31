from typing import TypeVar
from solution0006 import Solution0006
from solution0007 import Solution0007
from solution0010 import Solution0010
from solution0023 import Solution0023
# from solution0010naive import Solution0010Naive


Input = TypeVar("Input")
Output = TypeVar("Output")


def main():
    solutions = [
        Solution0006(),
        Solution0007(),
        # Solution0010Naive(),
        Solution0010(),
        Solution0023(),
    ]
    for solution in solutions:
        solution.run_tests()
        print()


if __name__ == "__main__":
    main()
