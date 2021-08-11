from dataclasses import dataclass

import pydash


@dataclass
class Node:
    host: str
    status: str


nodes = [Node("123.123.123.123", "OK"), Node("43.245.22.13", "DOWN"), Node("99.33.33.22", "OK")]

# returns the first element predicate returns truthy for
ok_nodes = pydash.find(nodes, lambda x: x.status == "OK")
print(ok_nodes)  # Node(host='123.123.123.123', status='OK')
