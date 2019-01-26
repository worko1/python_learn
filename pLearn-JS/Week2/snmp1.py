import pysnmp
from snmp_helper import snmp_get_oid,snmp_extract


COMMUNITY = 'ansible-r'
SNMP_PORT = 161
IP = '10.229.16.145'
OID = '1.3.6.1.2.1.1.5.0'

a_device= (IP, COMMUNITY , SNMP_PORT)
snmp_data = snmp_get_oid(a_device, oid=OID)
print(snmp_data)
print('\n')
print(snmp_extract(snmp_data))