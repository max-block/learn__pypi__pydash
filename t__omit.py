import pydash

d = {"a": 1, "b": 2, "c": 3, "d": 4}
print(pydash.omit(d, "a", "c"))
# {'b': 2, 'd': 4}
