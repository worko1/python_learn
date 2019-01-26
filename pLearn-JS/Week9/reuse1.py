import sys
from pprint import pprint
import ipaddress

# THESE are the IMPORTABLES =  functions
def func1():
    print "Function 1!"
    
def func2():
    print "Function 2!"

# MAIN function with all core structures
def main():
    
    pprint(sys.path)  # prints paths to libraries which are being used

    print(ipaddress.__file__)  # prints the path to where a given library is loaded from. In this case the lib "ipaddress"

print ("This is the __name__ var {}".format(__name__))

# THESE are the EXECUTABLES = in this case just the MAIN() function
if __name__ == "__main__":  # By default in case a different program wants to call the func1 or func2 and this "IF" is not set,
                            # the compiler reads and processes this whole PY file. If we use this "IF", it just processes 
                            # the called functions (func1 or func2)
    main()
                           


