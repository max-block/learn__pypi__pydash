import pydash

obj = {'a': 1, 'b': 2, 'c': 3}
new_obj = pydash.rename_keys(obj, {'a': 'A', 'b': 'B', "c": "cccc"})
print(new_obj)  # {'A': 1, 'B': 2, 'cccc': 3}
