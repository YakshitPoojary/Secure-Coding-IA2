import pickle

# Example of data received from an untrusted source (user input, network, etc.)
# Assume 'data' comes from an untrusted source
data = b"cos\nsystem\n(S'echo Insecure Deserialization!'\ntR."

# Deserialize the data
try:
    obj = pickle.loads(data)
    print("Deserialized object:", obj)
except Exception as e:
    print("Deserialization failed:", e)

# JSON deserialization (safe alternative)
data = '{"key": "value"}'
obj = json.loads(data)
print("Deserialized object:", obj)
