from typing import Iterator


class InventoryIterator(Iterator):
    def __init__(self, iterable: list):
        self.__iterable = iterable
        self.__index = 0

    def __next__(self):
        try:
            curr = self.__iterable[self.__index]
            self.__index += 1
            return curr
        except KeyError:
            raise StopIteration
