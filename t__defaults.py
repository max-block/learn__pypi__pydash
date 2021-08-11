import pydash

obj = {"a": None}
print(pydash.defaults(obj, {"a": 3, "b": 2}))
# {'a': None, 'b': 2}
