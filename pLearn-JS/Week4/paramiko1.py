import paramiko
from getpass import  getpass
from time import sleep

ip_addr = '10.229.16.145'
username = 'admin'
#password = getpass()
password = 'admin'
port = 22

remote_conn_pre = paramiko.SSHClient()  #create paramiko SSH object
remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # automatically adds unknown ssh keys to dbase

# establishes ssh connection
remote_conn_pre.connect(ip_addr, port=port, username=username, password=password, look_for_keys=False, allow_agent=False)

# ...
#remote_conn = remote_conn_pre.invoke_shell()

# reads from the SSH channels. Reads what ever data is available up to 5000 bytes. 
#outp = remote_conn.recv(5000)

#print (outp)

remote_connect = remote_conn_pre.invoke_shell()

print(remote_connect.recv_ready())
outp = remote_connect.recv(nbytes=5000)
print (outp)

outp2 = (remote_connect.send('show ip int br\n'))
sleep(1)
print(remote_connect.recv_ready())
print("{} bytes received!\n" .format(str(outp2)))
print(remote_connect.recv(nbytes=5000))

