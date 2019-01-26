import yaml

my_list = range(8)
my_list.append('whatever')
my_list.append('hallo')
my_list.append({})

my_list[-1]['ip_addr'] = '10.10.10.239'
my_list[-1]['attribs'] = range(7)

for item in my_list:
    print item

print ('The lenght of the list is .. {}'.format(len(my_list)))


print ('\n .. YAML output ..')
yam_test = yaml.dump(my_list, default_flow_style=False)
print yam_test

with open("some_file.yml", "w") as f:
    f.write("---\n\n")
    f.write(yaml.dump(my_list, default_flow_style=False))