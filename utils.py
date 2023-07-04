import json


def is_json_empty(json_data):
    # Convert JSON string to Python object
    data = json.loads(json_data)

    # Check if the JSON object is empty
    if len(data) == 0:
        return True
    else:
        return False
