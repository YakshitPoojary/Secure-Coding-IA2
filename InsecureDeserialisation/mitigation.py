import json
safe_data = json.dumps({"key": "value"})

def deserialize_safe(data):
    return json.loads(data)

print(deserialize_safe(safe_data))
