from __future__ import unicode_literals, print_function
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment


'''
interface GigabitEthernet0/1
 description {{ descript }}
 no switchport
 ip address {{ ip_addr }} {{ netmask }}
 speed auto
 duplex auto
!
{%- if vlan1 == True %}  {# the MINUS sign in %- does not leave a blank line in #}
interface Vlan1          {# the final output #}
 description **TEST VLAN1**
 ip address {{ vlan1_ip }} {{ vlan1_mask }}
 {%- if vlan1_v6 == True %}  {# nested IF #}
 ipv6 address {{ vlan1_v6_ip }}
 {%- endif %}
{%- elif vlan1 == False%}  {# ELIF for the main IF statement #}
interface Vlan1
 description **DHCP VLAN**
 ip address dhcp
{%- endif %}
'''

env = Environment(undefined=StrictUndefined)  # CREATE ENVIRONMENT: defines, that every variable {{}} in the template needs also strictly 
                                                # a variable value defined somewhere in the code/ Otherwise it will fail
# in case you don't want a strict behavior (variable may be missing), use just "env = Environment()"                                                 
                                                
env.loader = FileSystemLoader('.')  # WHERE TO FIND ENVIRONMENT: defines where the template to load from. 
                                    # In this case '.' it is in the current working directory


intf_vars = {
    'ip_addr' : '3.4.5.6',
    'netmask' : '255.255.255.192',
    'descript' : 'TEST 2 2 2 2',
    'vlan1' : False,
    'vlan1_ip' : '1.1.1.1',
    'vlan1_mask' : '255.255.0.0',
    'vlan1_v6' : False,
    'vlan1_v6_ip' : '0:0:0:0:0:ffff:304:506/64',
}

template_file = 'template_intf.j2'  # name of the template file
template = env.get_template(template_file)  # load the template file to the environment
output = template.render(**intf_vars)  # loads all attributes from dictionary intf_vars

print (output)