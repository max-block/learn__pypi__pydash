import pydash

d = {"a": 1, "b": 2, "c": 3, "d": 4}
print(pydash.pick(d, "a", "c"))
# {'a': 1, 'c': 3}
