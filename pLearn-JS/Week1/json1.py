import json

my_jlist = range(8)
my_jlist.append('whatever')
my_jlist.append('hallo')
my_jlist.append({})

my_jlist[-1]['ip_addr'] = '10.10.10.239'
my_jlist[-1]['attribs'] = range(5)

for item in my_jlist:
    print item
    
print ('\n .. JSON output ..')
jsn_test = json.dumps(my_jlist)
print jsn_test

with open("json_file.json", "w") as f:
    json.dump(my_jlist, f)