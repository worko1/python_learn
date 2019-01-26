import yaml

with open("some_file.yml" ,"r") as f:
    new_list = yaml.load(f)
    
for item in new_list:
    print item