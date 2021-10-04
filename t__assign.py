import pydash

obj1 = {"a": 1, "b":2}

print(pydash.assign(obj1, {"c": 3}))
# {'a': 1, 'b': 2, 'c': 3}
