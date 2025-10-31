from typing import List, Dict

class TodoItem:
    def __init__(self, id: int, title: str, done: bool = False):
        self.id = id
        self.title = title
        self.done = done

    def as_dict(self) -> Dict:
        return {"id": self.id, "title": self.title, "done": self.done}


class TodoService:
    def __init__(self):
        self._items: List[TodoItem] = []
        self._next_id = 1

    def list_items(self) -> List[Dict]:
        return [i.as_dict() for i in self._items]

    def get(self, todo_id: int):
        for item in self._items:
            if item.id == todo_id:
                return item.as_dict()

        return []

    def add(self, title: str) -> Dict:
        if not title or not isinstance(title, str):
            raise ValueError("title must be a non-empty string")
        item = TodoItem(self._next_id, title)
        self._items.append(item)
        self._next_id += 1
        return item.as_dict()

    def mark_done(self, item_id: int) -> Dict:
        for it in self._items:
            if it.id == item_id:
                it.done = True
                return it.as_dict()
        raise KeyError(f"item {item_id} not found")

    def clear(self):
        self._items = []
        self._next_id = 1