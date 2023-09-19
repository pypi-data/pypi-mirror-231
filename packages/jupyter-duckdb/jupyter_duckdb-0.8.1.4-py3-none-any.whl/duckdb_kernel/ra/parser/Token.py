class Token(str):
    def __new__(cls, value: str):
        # remove enclosing whitespaces and parentheses
        while True:
            value = value.strip()

            if len(value) > 2:
                if value[0] == '(' and value[-1] == ')':
                    value = value[1:-1]
                    continue

            return super().__new__(cls, value.strip())

    @property
    def empty(self) -> bool:
        return len(self) == 0

    @property
    def single_quotes(self) -> str:
        if self[0] != '"' or self[-1] != '"':
            return self
        else:
            return f"'{self[1:-1]}'"

    @property
    def clean(self) -> str:
        if len(self) > 2:
            if self[0] == '"' and self[-1] == '"':
                return self[1:-1]
            if self[0] == "'" and self[-1] == "'":
                return self[1:-1]

        return self

    def __getitem__(self, item) -> 'Token':
        return Token(super().__getitem__(item))
