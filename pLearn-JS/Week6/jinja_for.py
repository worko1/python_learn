from __future__ import unicode_literals, print_function
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment


'''
{%- for port_number in range(1, 49) %}
interface GigabitEthernet0/{{ port_number }}
 switchport mode access
 switchport access vlan {{ vlan_id }}
 spanning-tree portfast
 spanning-tree bpduguard enable
{%- endfor %}
'''

env = Environment(undefined=StrictUndefined)  # CREATE ENVIRONMENT: defines, that every variable {{}} in the template needs also strictly 
                                                # a variable value defined somewhere in the code/ Otherwise it will fail
# in case you don't want a strict behavior (variable may be missing), use just "env = Environment()"                                                 
                                                
env.loader = FileSystemLoader('.')  # WHERE TO FIND ENVIRONMENT: defines where the template to load from. 
                                    # In this case '.' it is in the current working directory


intf_vars = {
    'vlan_id' : '100',
}

template_file = 'switch_interfaces.j2'  # name of the template file
template = env.get_template(template_file)  # load the template file to the environment
output = template.render(**intf_vars)  # loads all attributes from dictionary intf_vars

print (output)