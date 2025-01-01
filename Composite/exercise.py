from abc import ABC
from collections.abc import Iterable


class ValueContainer(ABC, Iterable):
    @property
    def sum(self):
        result = 0
        for item in self:
            for value in item:
                result += value
        return result


class SingleValue(ValueContainer):
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        yield self.value


class ManyValues(list, ValueContainer):
    def __init__(self):
        super().__init__()


if __name__ == "__main__":
    pass
