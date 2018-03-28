import json
import sys


def load_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        json_data = f.read()
    serializable_object = json.loads(json_data)
    return serializable_object


def pretty_print_json(serializable_object):
    formatted_json = json.dumps(serializable_object, sort_keys=True, indent=4)
    return formatted_json


if __name__ == '__main__':
    path_for_file_with_json = sys.argv[1]
    print(pretty_print_json(load_data(path_for_file_with_json)))
