"""Holds JSON read and write functions"""
#Standart imports
import json

def write_value_to_json(filename, value):
    with open(filename, 'w') as f_obj:
        json.dump(value, f_obj)

def read_value_from_json(filename):
    try:
        with open(filename) as f_obj:
            return json.load(f_obj)
    except FileNotFoundError:
        return None