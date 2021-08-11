import pydash

arr = [
    {"id": 1, "name": "z"},
    {"id": 2, "name": "A"},
    {"id": 3, "name": "a"},
    {"id": 4, "name": "B"},
    {"id": 5, "name": "A"},
]

# sort by name (ignore case)

pydash.sort(arr, key=lambda x: x["name"].lower())
# it's the same code like: arr.sort(key=lambda x: x["name"].lower())
# don't use pydash for it!

print(arr)
# [{'id': 2, 'name': 'A'}, {'id': 3, 'name': 'a'}, {'id': 5, 'name': 'A'}, {'id': 4, 'name': 'B'}, {'id': 1, 'name': 'z'}] # noqa
