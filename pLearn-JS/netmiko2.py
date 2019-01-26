# multiline commands

from netmiko import Netmiko
from getpass import getpass

password = 'Hamburg2019+'
#password = getpass() # this method getpass() hides the typing of the pass on the screen

ham_sw = {
    'host': "192.168.219.1",
    'username': "worko",
    'password': password,
    'device_type': 'cisco_ios'
}

net_conn = Netmiko(**ham_sw)  # created an object of Netmiko
filename = 'vlan-tmp.dat'
cmd1 = 'delete flash:/vlan-tmp.dat'

#print(net_conn.find_prompt())    # prints the prompt

output = net_conn.send_command_timing(cmd1)
if 'filename' in output:
        output += net_conn.send_command_timing("\n\n")

net_conn.disconnect()
print(output)
print('---' *30)
