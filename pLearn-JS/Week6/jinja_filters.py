from __future__ import unicode_literals, print_function
import jinja2

'''
{% set new_mask = '/24' %}  # local variable
interface gigabit0/1
 description LAN connection
 ip address {{ ip_addr }}{{ new_mask }}
 duplex auto
 speed auto
'''


my_vars = {
    'router1' : 'cisco 881, hamburg, ger'  # definition of the attributes of device 'router1'    
}


my_template = '''
{{ router1 | upper}}      {# capitalizes all chars in the router1 attributes by applying jinja2 filter after the "|" sign #}
{{ router1 | capitalize}} {# capitalizes first character by applying filter #}
{{ router1 | center(80)}} {# centers whole output by applying filter #}
{{ router1 | center(80) | upper}} {# centers whole output + makes it upper case by applying filter #}
{{ router2 | default('NOT DEFINED DEVICE!')}}  {# throws an exception saying that the router2 is not defined #}
{{ "%30s %30s" | format(router1, "SECOND COLUMN!!") }}  {# puts the output of router1 in first column and second with a custom string #}
                                                        {# both columns are in this case 30-chars wide #}

'''


intf_vars = {
    'ip_addr' : '10.101.10.20',
    'netmask' : '255.255.248.0',
}


template = jinja2.Template(my_template)  # loads template
output = template.render(my_vars)
print (output)


with open("template_local_set.j2") as f:
    intf_config = f.read()

template2 = jinja2.Template(intf_config)  # read whatever is in the file defined as template
output2 = template2.render(**intf_vars)  # loads all attributes from dictionary intf_vars
print (output2)