import pydash

d = {"user": {"name": "Bill", "address": {"city": "Rome"}}}

print(pydash.get(d, "user.address.city"))  # Rome
print(pydash.get(d, "user.address2.city"))  # None


d = {"data": [{"name": "Bill", "age": 99}, {"name": "Bill2", "age": 88}]}
print(pydash.get(d, "data.0.name"))  # Bill
print(pydash.get(d, "data.1.age"))  # 88
