import json

def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r") as f:
        data = json.load(f)  
        return data

file_path = 'animals_data.json'
data = load_data(file_path)  

print(data)
