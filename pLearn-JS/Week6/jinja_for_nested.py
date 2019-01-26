from __future__ import unicode_literals, print_function
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment


'''
{%- for module, module_vars in modules.items() %}  {# the .items() is like calling dictionary values in Python and
{%- for port_number in module_vars['ports'] %}                    {# getting the corresp. key and its value back #}
interface GigabitEthernet{{ module }}/{{ port_number }}
 switchport mode access
 switchport access vlan {{ module_vars.vlan_id }}
 spanning-tree portfast
 spanning-tree bpduguard enable
!
{%- endfor %}
{%- endfor %}

{# TIP! the module_vars['ports'] can be written also as module_vars.ports #}
'''

env = Environment(undefined=StrictUndefined)  # CREATE ENVIRONMENT: defines, that every variable {{}} in the template needs also strictly 
                                                # a variable value defined somewhere in the code/ Otherwise it will fail
# in case you don't want a strict behavior (variable may be missing), use just "env = Environment()"                                                 
                                                
env.loader = FileSystemLoader('.')  # WHERE TO FIND ENVIRONMENT: defines where the template to load from. 
                                    # In this case '.' it is in the current working directory

#modules = [1, 2, 3, 4]

modules = {
    1: {'vlan_id' : 101, 'ports' : range(1, 12)},
    2: {'vlan_id' : 102, 'ports' : range(1, 13)},
    3: {'vlan_id' : 103, 'ports' : range(1, 14)},
    4: {'vlan_id' : 104, 'ports' : range(1, 15)},
    
}

intf_vars = {
    'modules' : modules,
    'vlan_id' : '100',
    'port_count' : '48',
}

template_file = 'switch_interfaces2.j2'  # name of the template file
template = env.get_template(template_file)  # load the template file to the environment
output = template.render(**intf_vars)  # loads all attributes from dictionary intf_vars

print (output)