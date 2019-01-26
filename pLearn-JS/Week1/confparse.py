# pip install ciscoconfparse
from ciscoconfparse import CiscoConfParse

cisco_cfg = CiscoConfParse("cisco.txt") # load configuration from cisco.txt to variable
intf = cisco_cfg.find_objects(r"interface") # find pattern interface
#
#
print(intf) # print lines including 'interface' in a HTML-like format
print("\n\n")

for item in intf:
    print item.text # print lines including 'interface' in a nice-looking format line-by-line (.text method)
#
#
gi04 = intf[8]  # 9th item of the list includes the gi0/4
print(gi04.text)

gi04_config = gi04.children # assign the variable the the gi0/4's configuration (.children method)

for child in gi04_config:  
    print child.text
#
# 
# find a parent which contains INTERFACE and has no IP Address
find_no_ip = cisco_cfg.find_objects_w_child(parentspec=r"interface", childspec=r"no ip address")
print ("\n....... NO IP ADDRESS Interfaces .......\n")
for item2 in find_no_ip:
    print item2.text
#
#
# find a parent which contains INTERFACE and has an IP Address
find_no_ip = cisco_cfg.find_objects_wo_child(parentspec=r"interface Gi", childspec=r"shutdown")
print ("\n....... NO SHUTDOWN Interfaces .......\n")
for item2 in find_no_ip:
    print item2.text
#
#
#
