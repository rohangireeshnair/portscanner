import socket
import argparse
import ipaddress as ip
import sysup


parser = argparse.ArgumentParser(description='Scan the system for vulnerable ports')
parser.add_argument('-x', help='To specify the upper limit of the port to be scanned.', type=int, default=1000)
args=parser.parse_args()


ipadr = input('Enter the IP Address of the target system :')

ntwrk = ip.ip_address(ipadr)
print('Checking if %s is up' % ipadr)
if(sysup.sysupcheck(ipadr)==0):
    print('Initiating port scan')

