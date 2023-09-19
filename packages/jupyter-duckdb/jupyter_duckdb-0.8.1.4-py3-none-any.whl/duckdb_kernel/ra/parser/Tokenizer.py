import re
from typing import Optional, List, Iterator

from .Token import Token


class Tokenizer:
    @staticmethod
    def tokenize(query: Token) -> Iterator[Token]:
        stack = Tokenizer()
        index, start = 0, 0
        query_len = len(query)

        while index < query_len:
            offset = stack(query[index])
            if offset >= 0:
                token = query[start:index + 1 - offset]
                if not token.empty:
                    yield token

                index -= offset
                start = index + 1

            index += 1

        if start <= index:
            token = query[start:index + 1]
            if not token.empty:
                yield token

    def __init__(self):
        self.stack: List[str] = []
        self.escape: bool = False
        self.special_characters: int = 0
        self.special_character_re: re.Pattern = re.compile(r'''[^A-Za-zÄÖÜäöüß0-9_()"']''')

    @property
    def last_character(self) -> Optional[str]:
        if len(self.stack) > 0:
            return self.stack[-1]

    @property
    def _in_single_quotes(self) -> bool:
        return self.last_character == "'"

    @property
    def _in_double_quotes(self) -> bool:
        return self.last_character == '"'

    @property
    def _in_parentheses(self) -> bool:
        for c in self.stack:
            if c == '(':
                return True

        return False

    def __call__(self, character: Token) -> int:
        in_single_quotes = self._in_single_quotes
        in_double_quotes = self._in_double_quotes
        in_parentheses = self._in_parentheses
        in_quotes = in_single_quotes or in_double_quotes
        in_single_quotes_or_parentheses = in_single_quotes or in_parentheses
        in_double_quotes_or_parentheses = in_double_quotes or in_parentheses
        in_quotes_or_parentheses = in_quotes or in_parentheses

        # abort if last character was an escape character
        if self.escape:
            self.escape = False
            return -1

        # escape characters
        if not in_quotes_or_parentheses and character == '\\':
            self.escape = True
            self.special_characters = 0
            return 1

        # collect special characters
        if not in_quotes_or_parentheses and self.special_characters:
            if not self.special_character_re.fullmatch(character):
                self.special_characters = 0
                return 1
            else:
                self.special_characters += 1
                return -1

        # single quotes
        if not in_double_quotes_or_parentheses and character == "'":
            if self._in_single_quotes:
                self.stack.pop()
                return 0
            else:
                self.stack.append(character)
                return -1

        # double quotes
        if not in_single_quotes_or_parentheses and character == '"':
            if self._in_double_quotes:
                self.stack.pop()
                return 0
            else:
                self.stack.append(character)
                return -1

        # parentheses
        if not in_quotes:
            if character == '(':
                self.stack.append(character)
                return -1

            if character == ')':
                if self.last_character == '(':
                    self.stack.pop()
                    return 0 if not self._in_parentheses else -1

                raise ValueError

        # whitespaces
        if not in_quotes_or_parentheses and character.empty:
            return 0

        # special characters that break tokens
        if not in_quotes_or_parentheses and self.special_character_re.fullmatch(character):
            self.special_characters = 1
            return 1

        return -1
