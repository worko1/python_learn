from __future__ import unicode_literals, print_function
import jinja2

intf_config = """
interface GigabitEthernet0/1
 description TEST-Learn
 no switchport
 ip address {{ ip_addr }} {{ netmask }}
 speed auto
 duplex auto
"""

intf_vars = {
    'ip_addr' : '2.2.2.2',
    'netmask' : '255.255.255.248',
}

template = jinja2.Template(intf_config)  # loads template
output = template.render(intf_vars)  # loads all attributes from dictionary intf_vars

print (output)