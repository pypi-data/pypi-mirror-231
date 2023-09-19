from typing import Tuple

from .Operand import Operand
from .Operator import Operator
from .operators import *
from .parser import *


# Instead of multiple nested loops, a tree with rotation can
# probably be used with less time complexity.

class RA:
    @staticmethod
    def _find(query: str, index: int, symbols: Tuple[str]) -> bool:
        for symbol in symbols:
            if len(query) - index < len(symbol):
                continue
            if query[index:index + len(symbol)].lower() == symbol:
                return True

        return False

    @staticmethod
    def parse(query: str) -> Element:
        initial_token = Token(query)
        return RA._parse(initial_token)

    @staticmethod
    def _parse(*tokens: Token, target: Operator | Operand = None) -> Element:
        print('in ', tokens)
        if len(tokens) == 1:
            tokens = tuple(Tokenizer.tokenize(tokens[0]))
        print('out', tokens)

        # binary operators
        for operator in BINARY_OPERATORS:
            # iterate tokens and match symbol
            for i in range(1, len(tokens) + 1):
                if tokens[-i].lower() in operator.symbols():
                    # return the operator
                    # with left part of tokens and right part of tokens
                    return operator(
                        RA._parse(*tokens[:-i]),
                        RA._parse(*tokens[-i + 1:])
                    )

        # unary operators
        for i in range(1, len(tokens) + 1):
            # iterate operators and match token
            for operator in UNARY_OPERATORS:
                if tokens[-i].lower() in operator.symbols():
                    # If no target from a previous step is handed over
                    # the last token is the operators target.
                    if target is None:
                        op = operator(
                            RA._parse(tokens[-1]),
                            RA._parse_arg(*tokens[-i + 1:-1])
                        )

                    # Otherwise the handed target is this operator's
                    # target.
                    else:
                        op = operator(
                            target,
                            RA._parse_arg(*tokens[-i + 1:])
                        )

                    # If there are any more tokens the operator is
                    # the target for the next step.
                    if i < len(tokens):
                        return RA._parse(
                            *tokens[:-i],
                            target=op
                        )

                    # Otherwise the operator is the return value.
                    else:
                        return op

        # return as name
        if len(tokens) > 1:
            raise AssertionError(f'{tokens=}')

        return Operand(tokens[0])

    @staticmethod
    def _parse_arg(*tokens: Token) -> Element:
        if len(tokens) == 1:
            tokens = tuple(Tokenizer.tokenize(tokens[0]))

        # logic operators
        for operator in LOGIC_OPERATORS:
            # iterate tokens and match symbol
            for i in range(1, len(tokens) + 1):
                if tokens[-i].lower() in operator.symbols():
                    # return the operator
                    # with left part of tokens and right part of tokens
                    return operator(
                        RA._parse_arg(*tokens[:-i]),
                        RA._parse_arg(*tokens[-i + 1:])
                    )

        # not
        if tokens[0] in LOGIC_NOT.symbols():
            return LOGIC_NOT(
                RA._parse_arg(*tokens[1:])
            )

        # ArgList
        return LogicOperand(*tokens)
