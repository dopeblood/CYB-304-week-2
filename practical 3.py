import json

data = '{"name": "Ayo", "age": 22}'

parsed = json.loads(data)

print(parsed["name"])