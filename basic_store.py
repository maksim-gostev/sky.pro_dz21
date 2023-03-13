from storage import Storage


class Basic_Store(Storage):
    def __init__(self, items: dict[str: int], capacity: int ):
        super().__init__(items, capacity)

    @property
    def items(self):
        return self._items

    @property
    def capacity(self):
        return self._capacity

    def get_free_space(self) -> int:
        free_space = self.capacity - sum(self.items.values())
        if free_space < 0:
            return 0
        return free_space

    def get_items(self) -> dict:
        return self.items

    def get_unique_items_count(self) -> int:
        return len(self.items)

    def add(self, title: str, quantity: int):
        if self.get_free_space() < quantity:
            return False

        if self.is_in_storage(title):
            self.items[title] += quantity
            return True
        else:
            self.items[title] = quantity
            return True


    def is_in_storage(self, title: str) -> bool:
        if title in self.items:
            return True
        return False

    def remove(self, title: str, quantity: int) -> bool:
        if not self.is_in_storage(title):
            return False

        if quantity > self.items[title]:
            return False

        self.items[title] -= quantity

        if self.items[title] == 0:
            del self.items[title]
        return True
