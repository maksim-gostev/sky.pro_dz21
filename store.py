from basic_store import Basic_Store

class Store(Basic_Store):
    def __init__(self, items: dict[str: int], capacity: int = 100):
        super().__init__(items, capacity)
