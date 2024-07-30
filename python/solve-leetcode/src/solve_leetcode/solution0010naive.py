from abc import ABC, abstractmethod
from solution import Solution


# List of possible matches in the form [(matched_text, remaining_text), ...]
RegexTestResult = list[tuple[str, str]] | None


def debug(*values: object):
    # print(*values)
    pass


class Regex(ABC):
    @abstractmethod
    def test(self, string: str) -> RegexTestResult:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass


class RegexCharacter(Regex):
    def __init__(self, character: str) -> None:
        self.character = character

    def test(self, string: str) -> RegexTestResult:
        if len(string) == 0:
            return None
        str_char = string[0]

        if (self.character == ".") or str_char == self.character:
            return [(str_char, string[1::])]

    def __str__(self) -> str:
        return self.character


class RegexStar(Regex):
    def __init__(self, repeated_regex: Regex) -> None:
        self.repeated_regex = repeated_regex

    def __str__(self) -> str:
        return str(self.repeated_regex) + "*"

    def test(self, string: str) -> RegexTestResult:
        def test_recursive(
            previous_matched_text: str, remaining_text: str
        ) -> RegexTestResult:
            if remaining_text == "":
                return []

            regex_result = self.repeated_regex.test(remaining_text)
            debug(
                f"[{self.__class__.__name__}] previous_matched_text, regex_result: '{previous_matched_text}', '{regex_result}'"
            )
            if regex_result is None:
                return []

            matches: RegexTestResult = regex_result[::]
            for matched_text, matched_remaining_text in regex_result:
                total_matched_text = previous_matched_text + matched_text
                # matches.append((total_matched_text, matched_remaining_text))

                debug(
                    f'[{self.__class__.__name__}] total_matched_text, remaining_text : "{total_matched_text}", "{matched_remaining_text}"'
                )
                next_regex_result = test_recursive(
                    total_matched_text, matched_remaining_text
                )
                if next_regex_result is not None:
                    debug(
                        f"[{self.__class__.__name__}] extending matches with {next_regex_result}"
                    )
                    matches.extend(next_regex_result)

            return matches

        result = [("", string)]
        result.extend(test_recursive("", string) or [])

        debug(f"[{self.__class__.__name__}] results ", result)
        return result


class RegexSequence(Regex):
    def __init__(self, elements: list[Regex]) -> None:
        self.elements = elements

    def __str__(self) -> str:
        string = ""
        for element in self.elements:
            string += str(element)
        return string

    def test(self, string: str) -> RegexTestResult:
        def test_recursive(
            previous_matched_text: str, elements: list[Regex], remaining_text: str
        ) -> RegexTestResult:
            if len(elements) == 0:
                if remaining_text == "":
                    debug(
                        f"[{self.__class__.__name__}] no remaining text, previous_matched_text='{previous_matched_text}'"
                    )
                    # return []
                    return [(previous_matched_text, "")]
                return None

            element = elements.pop(0)
            element_matches = element.test(remaining_text)

            debug(
                f"[{self.__class__.__name__}] previous_matched_text, element_matches: '{previous_matched_text}', '{element_matches}' "
            )

            if element_matches is None:
                return None

            # if remaining_text == '' and len(elements) == 0:
            #     return None

            for element_matched_text, element_remaining_text in element_matches:
                result_with_this_match = test_recursive(
                    previous_matched_text + element_matched_text,
                    elements[::],
                    element_remaining_text,
                )
                if result_with_this_match is not None:
                    for _next_matched, next_remaining in result_with_this_match:
                        debug(
                            f"[{self.__class__.__name__}] _next_matched, next_remaining: '{_next_matched}', '{next_remaining}'  "
                        )
                        if next_remaining == "":
                            return [(previous_matched_text + remaining_text, "")]

            return None

        return test_recursive("", self.elements[::], string)


def parse_regex(pattern: str) -> RegexSequence:
    pattern_len = len(pattern)
    index = 0
    elements: list[Regex] = []

    while index < pattern_len:
        pattern_char = pattern[index]

        if pattern_char == "." or pattern_char.isalpha():
            next_char_index = index + 1
            if next_char_index < pattern_len and pattern[next_char_index] == "*":
                elements.append(RegexStar(RegexCharacter(pattern_char)))

                index += 1
                while (
                    next_char_index + 1 < pattern_len
                    and pattern[next_char_index + 1] == "*"
                ):
                    next_char_index += 1
                    index += 1
            else:
                elements.append(RegexCharacter(pattern_char))
        else:
            raise Exception(
                "shouldn't happen if * is not first char and input is alphabet char"
            )

        index += 1

    return RegexSequence(elements)


test_cases_0010 = [
    (("a", "b"), False),
    (("aa", "a"), False),
    (("a", "aa"), False),
    (("", "a"), False),
    (("a", ""), False),
    (("a", "a"), True),
    (("a", "."), True),
    (("", "a*"), True),
    (("a", "a*"), True),
    (("aa", "a*"), True),
    (("b", "a*a"), False),
    (("", "a*a"), False),
    (("a", "a*a"), True),
    (("aa", "a*a"), True),
    (("aaa", "a*a"), True),
    (("aa", "a*b"), False),
    (("ab", "abc*d"), False),
    (("abc", "abc*d"), False),
    (("abd", "abc*d"), True),
    (("abcd", "abc*d"), True),
    (("abccd", "abc*d"), True),
    (("d", "c*d"), True),
    (("cd", "c*d"), True),
    (("ccd", "c*d"), True),
    (("ab", ".*"), True),
    (("bb", "a*.*"), True),
    (("aaaaa", "a**"), True),
    (("aaaaaaaaaaaaaaaaaaab", "a*a*a*a*"), False),
    (("aaaaaaaaaaaaaaaaaaab", "a*a*a*a*a*a*"), False),
    (("ab", "a*a*a*a*a*a*a*a*a*a*"), False),
    (("aaaaaab", "a*a*a*a*a*a*a*a*a*a*"), False),
    (("aaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*"), False),
    (("aaaaaaaaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*"), False),
    (("aaaaaaaaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*b*a*"), True),
]


class Solution0010Naive(Solution[tuple[str, str], bool]):
    def __init__(self) -> None:
        super().__init__(test_cases_0010)

    def solve(self, input: tuple[str, str]) -> bool:
        string, pattern = input
        regex = parse_regex(pattern)
        result = regex.test(string)

        if result is not None:
            result.reverse()
            for _matched_text, remaining_text in result:
                if remaining_text == "":
                    return True

        return False
