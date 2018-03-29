import json
import argparse
import os
from argparse import ArgumentTypeError
from json.decoder import JSONDecodeError


class FileExist(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        prospective_path_to_file = values
        class_name = self.__class__.__name__
        err_mes_template = '{class_name}: {path} {problem}'
        if not os.path.isfile(prospective_path_to_file):
            problem_description = 'is not valid path'
            err_mes = err_mes_template.format(class_name=class_name,
                                              path=prospective_path_to_file,
                                              problem=problem_description)
            raise ArgumentTypeError(err_mes)
        if os.access(prospective_path_to_file, os.R_OK):
            setattr(namespace, self.dest, prospective_path_to_file)
        else:
            problem_description = 'is not a readable file'
            err_mes = err_mes_template.format(class_name=class_name,
                                              path=prospective_path_to_file,
                                              problem=problem_description)
            raise ArgumentTypeError(err_mes)


def get_arg_parser():
    default_file_path = './test.json'
    arg_parser = argparse.ArgumentParser(description='Convert JSON data to human-readable form')
    arg_parser.add_argument('-f', '--data_file',
                            action=FileExist, default=default_file_path,
                            help='path to file with JSON string')
    return arg_parser


def get_data_file_path():
    args = get_arg_parser().parse_args()
    return args.data_file


def get_serializable_object_from_file(file_path):
    with open(file_path, 'r') as file:
        json_data = file.read()
        deserialized_object = json.loads(json_data)
    return deserialized_object


def get_formatted_json(deserialized_object):
    formatted_json = json.dumps(deserialized_object, sort_keys=True, indent=4, ensure_ascii=False)
    return formatted_json


if __name__ == '__main__':
    try:
        path_to_file_with_json = get_data_file_path()
    except ArgumentTypeError as exc:
        print("Sorry, but it's problem with file: {}".format(exc))
    else:
        try:
            print(get_formatted_json(get_serializable_object_from_file(path_to_file_with_json)))
        except JSONDecodeError as exc:
            print("Sorry, but it's problem with your JSON: {}".format(exc))
