import pydash

arr = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8]

print(pydash.pull(arr, 3, 4, 5))  # [1, 2, 6, 7, 8]
