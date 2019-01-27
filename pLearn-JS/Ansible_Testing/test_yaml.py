import yaml
from pprint import pprint

y_filename = raw_input('Enter filaname:')
# y_filename='yaml_file.yml'

def read_yaml(input_file):
    with open(input_file ,"r") as f:
        return (yaml.load(f))

pprint(read_yaml(y_filename))