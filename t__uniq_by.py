import pydash

d1 = {"name": "d1", "value": 1}
d2 = {"name": "d2", "value": 2}
d3 = {"name": "d3", "value": 1}
d4 = {"name": "d4", "value": 4}
d5 = {"name": "d5", "value": 5}
d_arr = [d1, d2, d3, d4, d5, d1, d2, d3, d4, d5]

print(pydash.uniq_by(d_arr, lambda x: x["value"]))
