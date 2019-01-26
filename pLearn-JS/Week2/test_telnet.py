import telnetlib
import time
from time import sleep
import socket
import sys


def output_screen(remote_conn, cmd):
    remote_conn.write(cmd + "\n")
    time.sleep(1)
    output_screen = remote_conn.read_very_eager()
    return (output_screen)


def login(remote_conn , user_name , passw):
    output_login = remote_conn.read_until("Username:", timeout=6)
    remote_conn.write(user_name + '\n')
    output_login = remote_conn.read_until("Password:", timeout=6)
    remote_conn.write(passw + '\n')
    return (output_login)

def telnet_connect(ip_address):
    try:
        return telnetlib.Telnet(ip_address, timeout=3)
    except socket.timeout:
        sys.exit("Connection has timed-out bitch!!!")
    except socket.error:
        sys.exit("Connection REFUSED bitch!!!")

def main():
    username = 'admin'
    password = 'admin'
    ip_addr = raw_input("Enter IP address:") 
    # '10.229.16.145'
    
    remote_conn = telnet_connect(ip_addr)
        
    login(remote_conn, username, password)
        
    time.sleep(1)
        
    remote_conn.write("term length 0" + "\n")
    command_in = raw_input("Enter command to SHOW:")
    #print(command_in)
    sleep(2)
    print(output_screen(remote_conn, command_in))


    remote_conn.close()
    
if __name__ == "__main__":
    main()