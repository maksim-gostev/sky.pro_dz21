from abc import ABC, abstractmethod


class Storage(ABC):
    def __init__(self, items: dict[str: int], capacity: int):
        self._items = items
        self._capacity = capacity

    @property
    @abstractmethod
    def items(self):
        return self._items

    @property
    @abstractmethod
    def capacity(self):
        return self._capacity

    @abstractmethod
    def add(self, title: str, quantity: int):
        """
        увеличивает запас items
        :param title:название
        :param quantity:количество
        :return:str
        """
        pass

    @abstractmethod
    def remove(self, title: str, quantity: int):
        """
        уменьшает запас items
        :param title:название
        :param quantity:количество
        :return:str
        """
        pass

    @abstractmethod
    def get_free_space(self) -> int:
        """
        вернуть количество свободных мест
        :return:int
        """
        pass

    @abstractmethod
    def get_items(self) -> dict:
        """
        возвращает сожержание склада в словаре {товар: количество}
        :return:dict
        """
        pass

    @abstractmethod
    def get_unique_items_count(self) -> int:
        """
        возвращает количество уникальных товаров
        :return: int
        """
        pass

    @abstractmethod
    def is_in_storage(self, title: str) -> bool:
        pass
