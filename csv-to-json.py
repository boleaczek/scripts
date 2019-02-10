import csv
import json
import helpers
import sys

bool_true = "True"
bool_false = "False"
separator = " "
indent = 4

def get_conversion_method(item_type):
    if  item_type == "string":  
        conversion = lambda item : item
    elif item_type.lower() == "numberi":
        conversion = int
    elif item_type.lower() == "numberf":
        conversion = float
    elif item_type.lower() == "bool":
        conversion = string_to_bool

    return conversion

def string_to_bool(string):
    if string.strip() == bool_true:
        return True
    elif string == bool_false:
        return False

def string_to_array(string, item_type):
    string = string.strip()[1:-1]
    items = string.split(",")
    conversion = get_conversion_method(item_type)
    
    converted_items = []
    for item in items:
        print(item)
        converted_items.append(conversion(item))
    return converted_items

def csv_row_to_json(row, names, item_types):
    row_dict = {}

    for value, name, item_type in zip(row, names, item_types):
        name = name.strip()
        item_type = item_type.strip()
        if item_type.startswith("["):
            row_dict[name] = string_to_array(value, item_type[1:-1])
        else:
            conversion = get_conversion_method(item_type.strip())
            row_dict[name] = conversion(value)

    return json.dumps(row_dict, indent = indent)

def csv_to_json(filename):
    json = []
    with open(filename) as csvfile:
        rows = csv.reader(csvfile, delimiter = separator)
        names = next(rows)
        types = next(rows)
        for row in rows:
            json.append(csv_row_to_json(row, names, types))
    return json


csv_filename = sys.argv[1]
output_filename = sys.argv[2]
print(f"Input: {csv_filename}\nOutput: {output_filename}")

params = sys.argv[3:]
expectedParams = {'s','b'}
found_params = helpers.getMarkedParams(params, expectedParams)

if 'b' in found_params:
    bool_tf = found_params['b'].split(":")
    bool_true = bool_tf[0]
    bool_false = bool_tf[1]
print(f"{bool_true} means True, {bool_false} means False")

if 's' in found_params:
    separator = found_params['s']
print(f"Using {separator} as separator")

output = open(output_filename, "w+")

json_objects = csv_to_json(csv_filename)
for json_object in json_objects:
    output.write(json_object + ',' + '\n')