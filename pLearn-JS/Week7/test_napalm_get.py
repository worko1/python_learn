from __future__ import print_function
from __future__ import unicode_literals

from getpass import getpass
from pprint import pprint
from napalm import get_network_driver
from pyeapi.eapilib import CommandError
import re

def wrapper_func(napalm_obj, napalm_method, banner=""):
    my_method = getattr(napalm_obj, napalm_method)
    print()
    print(banner.center(80, '-'))
    pprint(my_method())
    print('-' * 80)
    print()

test_methods = [
    "get_arp_table",
    "get_mac_address_table",
    "get_interfaces",
    "get_users",
    "get_config"
    ]
    

#my_password = getpass()
my_password = 'admin'

cisco_sw = dict(  # Create a dictionary containing switche's information
    hostname='10.229.16.145',
    device_type='ios',  # uses Netmiko, or basically SSH under the hood
    username='admin',
    password=my_password,
    opt_args={}
    )


devices = [cisco_sw]  # Tuple for the defined devices. In this case there is just one = cisco_sw

napalm_conns = []  # Keeps track of the open connections

for a_device in devices:
    driver = get_network_driver(a_device['device_type']) # obtain the proper network driver from the device_type
    # make the NAPALM call by passing all the device's connection params (hostname, pass, etc)
    device = driver(a_device['hostname'], a_device['username'], a_device['password'], timeout=60, optional_args=a_device['opt_args'])
    napalm_conns.append(device)  # adds this device to the connection list to keep track of it
    
    print()
    print("\n\n>>>Test device open<<<")
    device.open()  # opens the NAPALM connection
    
    print()
    banner = " Facts {}" .format(a_device['device_type'])
    print(banner.center(80, '-'))
    #pprint(device.get_users())
    for my_methods in test_methods:
        banner_for = " Method - {}" .format(my_methods)
        print(banner_for.center(80, '-'))
        output_method = "device." + my_methods + '()'
        pprint(eval(output_method))
        raw_input("Hit ENTER to continue: ")
    print('-' * 80)
    print()
    
raw_input("Hit ENTER to continue: ")


