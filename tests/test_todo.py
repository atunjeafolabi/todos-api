import pytest
from app.todo import TodoService


def test_add():
    s = TodoService()
    s.clear()
    item = s.add("buy milk")

    assert item["title"] == "buy milk"
    assert item["id"] == 1


def test_list_todos():
    s = TodoService()
    s.clear()
    todo_item1 = s.add("get some groceries")
    todo_item2 = s.add("do the dishes")
    todo_item3 = s.add("throw away the thrash")

    items = s.list_items()
    assert len(items) == 3
    assert [todo_item1, todo_item2, todo_item3] == items


def test_mark_as_done():
    s = TodoService()
    s.clear()
    item = s.add("feed the cats")
    id = item["id"]
    print(s.list_items())
    todo_item = s.get(id)

    assert todo_item["done"] is False
    marked = s.mark_done(id)
    assert marked["done"] is True