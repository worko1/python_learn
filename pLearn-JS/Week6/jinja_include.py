from __future__ import unicode_literals, print_function
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment


''' 
>> nxos_bgp_include.j2 <<
feature bgp
router bgp {{ local_as }}
 {% include 'bgp_ipv4_routes.j2' %}  {# appends a separate FILE's content on this place #}
 neighbor {{ peer1_ip }} remote-as {{ peer1_as }}
   update-source loop1
   ebgp-multihop 2
   address-family ipv4 unicast
!
{%- include eigrp_template %}   {# eigrp_template is a VARIABLE defined in the dictionary #}

>> bgp_ipv4_routes.j2 <<
address-family ipv4 unicast
   network {{ advertised_route1 }}
   network {{ advertised_route2 }}
   network {{ advertised_route3 }}
   
>> eigrp_template1.j2 <<
router eigrp 1
 !
 address-family ipv4 vrf CORP 
  network 10.115.79.49 0.0.0.0
  network 10.115.79.170 0.0.0.0
  network 10.115.79.174 0.0.0.0
  !
  network 10.115.68.0 0.0.0.255
  network 10.115.78.0 0.0.0.255
  passive-interface default
  no passive-interface Vlan920
  no passive-interface Vlan921
  autonomous-system 1
  eigrp router-id 10.115.79.49
  eigrp stub connected summary
  nsf
 exit-address-family
 !

'''

env = Environment(undefined=StrictUndefined)  # CREATE ENVIRONMENT: defines, that every variable {{}} in the template needs also strictly 
                                                # a variable value defined somewhere in the code/ Otherwise it will fail
# in case you don't want a strict behavior (variable may be missing), use just "env = Environment()"                                                 
                                                
env.loader = FileSystemLoader('.')  # WHERE TO FIND ENVIRONMENT: defines where the template to load from. 
                                    # In this case '.' it is in the current working directory

bgp_vars = {
    'hostname' : 'test-rt1',
    'local_as' : '10',
    'peer1_ip' : '10.255.255.2',
    'peer1_as' : '20',
    'advertised_route1' : '10.10.200.0/24',
    'advertised_route2' : '10.10.201.0/24',
    'advertised_route3' : '10.10.202.0/24',
    'eigrp_template' : 'eigrp_template1.j2',
    
}

template_file = 'nxos_bgp_include.j2'  # name of the template file
template = env.get_template(template_file)  # load the template file to the environment
output = template.render(**bgp_vars)  # loads all attributes from dictionary intf_vars
print (output)