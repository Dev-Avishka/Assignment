import json

def readjsonfile(path):
    try:
        with open(path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        raise FileNotFoundError(f"The file at {path} was not found")
    except json.JSONDecodeError:
        raise ValueError(f"The file at {path} contains invalid JSON")
    except Exception as e:
        raise Exception(f"An error occurred while reading the file: {str(e)}")
