import json

def read_print_pretty_json(file_path):
    """
    Reads a JSON file, outputs error message
    """
    try:
        with open(file_path, 'r') as file:
            pretty_json = json.load(file)      
    except Exception as e:
        print(f"An error occurred: {e}")

    return pretty_json
pretty_json = read_print_pretty_json('testDataset.json')
print(type(pretty_json))

def unpack_dict(d, indent=0):
    for key, value in d.items():
        print(' ' * indent + str(key) + ':', end=' ')
        if isinstance(value, dict):
            print()
            unpack_dict(value, indent + 4)
        elif isinstance(value, list):
            print()
            unpack_list(value, indent + 4)
        else:
            print(value)

def unpack_list(l, indent=0):
    for item in l:
        if isinstance(item, dict):
            unpack_dict(item, indent)
        elif isinstance(item, list):
            unpack_list(item, indent)
        else:
            print(' ' * indent + str(item))

unpack_dict(pretty_json)


