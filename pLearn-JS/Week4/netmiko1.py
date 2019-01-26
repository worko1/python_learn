from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint

AnsibleSW = {
    'device_type' : 'cisco_ios',
    'ip' : '10.229.16.145',
    'username' : 'admin',
    'password' : 'admin',
    'port' : '22',
    }

ansiblesw_connect = ConnectHandler(**AnsibleSW)  # passes login credentials as the whole "AnsibleSW" dictionary 
#pprint (dir(ansiblesw_connect))  # prints all the methods associated with the above object

print (ansiblesw_connect.find_prompt())  # shows the current level of configuration mode

ansiblesw_connect.config_mode()  # enters cisco's configuration mode
print(ansiblesw_connect.check_config_mode())  #checks if the app is currently in the config mode or not
print (ansiblesw_connect.find_prompt())  # prints the actual mode level

ansiblesw_connect.exit_config_mode()  # exits cisco's configuration mode
print (ansiblesw_connect.find_prompt())  # prints the actual mode level

output1 = ansiblesw_connect.send_command("show ver") # sends desired command and automatically adds a new line at the end
print(output1)                                                # + it disables automatically paging (term length 0)


config_command = ['loggin buffer 4096']  # creates a list of commands to send to the device
send1 = ansiblesw_connect.send_config_set(config_command)  # establishes the sending of the command defined above
output2 = ansiblesw_connect.send_command("show logg | i uffe") # send command to check the result of the change
print(output2)  # print the outputed change