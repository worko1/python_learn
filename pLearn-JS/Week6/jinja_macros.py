from __future__ import unicode_literals, print_function
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment


'''
# macros are as functions as Python
{%- macro intf_trunk(native_vlan=1, trunk_allowed_vlans=1) -%}  # macro definitions with default values
 switchport mode trunk
 switchport trunk native vlan {{ native_vlan }}
 switchport trunk allowed vlan {{trunk_allowed_vlans }}
{%- endmacro %}
{%- macro intf_access(vlan=1) -%}
 switchport mode access
 switchport access vlan {{ vlan }}
{%- endmacro %}
!
!
!
interface gigabit0/1  # interfaces definitions with custom values which will be put inside the script instead of the defaults
 {{ intf_trunk(native_vlan=1, trunk_allowed_vlans="1,100") }}
!
interface gigabit0/2
 {{ intf_trunk(native_vlan=10, trunk_allowed_vlans="1,200,300") }}
!
interface gigabit0/3
 {{ intf_access() }}
!
interface gigabit0/4
 {{ intf_access(vlan=202) }}
'''

env = Environment(undefined=StrictUndefined)  # CREATE ENVIRONMENT: defines, that every variable {{}} in the template needs also strictly 
                                                # a variable value defined somewhere in the code/ Otherwise it will fail
# in case you don't want a strict behavior (variable may be missing), use just "env = Environment()"                                                 
                                                
env.loader = FileSystemLoader('.')  # WHERE TO FIND ENVIRONMENT: defines where the template to load from. 
                                    # In this case '.' it is in the current working directory


device_vars = {}

template_file = 'interface_macro.j2'  # name of the template file
template = env.get_template(template_file)  # load the template file to the environment
output = template.render(device_vars)

print (output)