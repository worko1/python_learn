from snmp_helper import snmp_get_oid_v3,snmp_extract


if True:
    IP = '10.229.16.145'
    OID = '1.3.6.1.2.1.1.5.0'
    a_user = 'snmp_user'
    auth_key = 'snmp_pass'
    encrypt_key = 'snmp_pass2'
    snmp_usr = (a_user, auth_key, encrypt_key)
    switch1 = (IP, 161)

snmp_data = snmp_get_oid_v3(switch1, snmp_usr, oid=OID)

print(snmp_data)
print('\n')
print(snmp_extract(snmp_data))


snmp_oids = (
            ('sysName' , '1.3.6.1.2.1.1.5.0' , None),
            ('sysUptime' , '1.3.6.1.2.1.1.5.0' , None),
            ('ifDesc' , '1.3.6.1.2.1.1.5.0' , None),
            ('sysName' , '1.3.6.1.2.1.1.5.0' , None),
            ('sysName' , '1.3.6.1.2.1.1.5.0' , None),
            ('sysName' , '1.3.6.1.2.1.1.5.0' , None),
            ('sysName' , '1.3.6.1.2.1.1.5.0' , None),
            ('sysName' , '1.3.6.1.2.1.1.5.0' , None),
    )