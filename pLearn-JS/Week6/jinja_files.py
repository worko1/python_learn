from __future__ import unicode_literals, print_function
import jinja2


'''
intf_config = """
interface GigabitEthernet0/1
 description {{ descript }}
 no switchport
 ip address {{ ip_addr }} {{ netmask }}
 speed auto
 duplex auto

"""
'''

with open("template_jinja.j2") as file:  # read whatever is in the file defined as template
    intf_config = file.read()

intf_vars = {
    'ip_addr' : '2.2.2.2',
    'netmask' : '255.255.255.248',
    'descript' : 'TEST TEST TEST',
}

template = jinja2.Template(intf_config)  # loads template
output = template.render(**intf_vars)  # loads all attributes from dictionary intf_vars

print (output)