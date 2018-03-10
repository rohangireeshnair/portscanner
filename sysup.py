import os
import sys

def sysupcheck(ipadr):
    resp = os.system('ping -c 1 %s' % ipadr)
    if resp==0:
        print('System is up')
        return 0
    else:
        print('System is down. Program exiting')
        sys.exit(1)