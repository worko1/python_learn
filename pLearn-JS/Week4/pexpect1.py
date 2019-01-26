import pexpect
from getpass import getpass
import sys
import re

def main():
    ip_addr = '10.229.16.145'
    username = 'admin'
    #password = getpass()
    password = 'admin'
    port = 22

    ssh_connect = pexpect.spawn('ssh -l {} {} -p {}'.format(username, ip_addr, port))
    
    #ssh_connect.logfile = sys.stdout
    ssh_connect.expect('ssword', timeout=3)
    ssh_connect.sendline(password)
    ssh_connect.expect('#')
    print(ssh_connect.before)  # print what did the app see before the last expect = "#" sign
    print(ssh_connect.after)  # print what did the app see after the last expect = "#" sign

    ssh_connect.sendline('term length 0')  # it is neccessary to print longer outputs which are ending with '#' at the end
    ssh_connect.expect('#')                # otherwise they will not end wit a '#' and the app will raise a timeout exception
        
    #try:
    #    ssh_connect.sendline('show version')
    #    ssh_connect.expect('zzzz', timeout=2)  #it will never come back a 'zzzz' string and so after 2s will raise exception
    #except pexpect.TIMEOUT:
    #    print ("Found timeout")
        
    pattern = re.compile(r'^.*ice.*', re.MULTILINE)
    ssh_connect.sendline('show version')
    ssh_connect.expect(pattern)
    print(ssh_connect.after)
    

if __name__ == "__main__":
    main()