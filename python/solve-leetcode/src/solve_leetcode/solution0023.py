from typing import List, Optional, Self
from solution import Solution


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: Optional[Self] = None):
        self.val = val
        self.next = next

    def __eq__(self, value: object, /) -> bool:
        if isinstance(value, ListNode):
            return self.val == value.val and self.next == value.next

        return False

    def __str__(self) -> str:
        return f"{self.val}, {self.next}"


class Solution0023(Solution[List[Optional[ListNode]], Optional[ListNode]]):
    def __init__(self) -> None:
        super().__init__(
            [
                (
                    [
                        ListNode(1, ListNode(4, ListNode(5))),
                        ListNode(1, ListNode(3, ListNode(4))),
                        ListNode(2, ListNode(6)),
                    ],
                    ListNode(
                        1,
                        ListNode(
                            1,
                            ListNode(
                                2,
                                ListNode(
                                    3,
                                    ListNode(4, ListNode(4, ListNode(5, ListNode(6)))),
                                ),
                            ),
                        ),
                    ),
                ),
                ([], None),
                ([None], None),
            ]
        )

    def solve(self, input: List[Optional[ListNode]]) -> Optional[ListNode]:
        lists = input

        def solve_recursive(
            lists: List[Optional[ListNode]], output_list_tail: Optional[ListNode]
        ) -> Optional[ListNode]:
            min_value_list = None
            min_value_list_index = None

            for list_index, list_node in enumerate(lists):
                if list_node is None:
                    continue
                list_node_value = list_node.val
                if min_value_list is None or list_node_value < min_value_list.val:
                    min_value_list = list_node
                    min_value_list_index = list_index

            if min_value_list is None or min_value_list_index is None:
                return None
            lists[min_value_list_index] = min_value_list.next

            if output_list_tail is not None:
                output_list_tail.next = min_value_list

            min_value_list.next = solve_recursive(lists, min_value_list)

            return min_value_list

        return solve_recursive(lists, None)
