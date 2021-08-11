import pydash

arr = [{"a": 1, "b": 2}, {"a": 3, "b": 4}, {"a": 5, "b": 6}]

pydash.remove(arr, lambda x: x["b"] == 4)
print(arr)
# [{'a': 1, 'b': 2}, {'a': 5, 'b': 6}]
