import paramiko
from getpass import  getpass
from sys import stdin, stdout, stderr
from pprint import pprint
from time import sleep

ip_addr = '10.229.16.145'
username = 'admin'
#password = getpass()
password = 'admin'
port = 22

remote_conn_pre = paramiko.SSHClient()  #create SSH object
remote_conn_pre.load_system_host_keys()# automatically checks the local user's host-key file

# establishes ssh connection
remote_conn_pre.connect(ip_addr, port=port, username=username, password=password, look_for_keys=False,auth_timeout=5, allow_agent=False)

'''
stdin, stdout, stderr = remote_conn_pre.exec_command("sh ip int br\n")
print(stdout.read())
'''
remote_connect = remote_conn_pre.invoke_shell()

#print(remote_connect.recv_ready())
#outp = remote_connect.recv(nbytes=5000)
#print (outp)

outp2 = (remote_connect.send('term length 0\n'))
outp2 = (remote_connect.send('show run\n'))
sleep(1)
print(remote_connect.recv_ready())
print("{} bytes received!\n" .format(str(outp2)))
print(remote_connect.recv(nbytes=50000))


remote_conn_pre.close()