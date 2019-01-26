import json
from pprint import pprint as pp


with open("json_file.json") as f:
    jnew_list = json.load(f)

pp(jnew_list)
#for jitem in jnew_list:
#    pp  jitem