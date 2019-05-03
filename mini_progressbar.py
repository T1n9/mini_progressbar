
import sys
import time
 
 
def progressbar(str):
    sys.stdout.write("\r{0}".format(str))
    sys.stdout.flush()
    sys.stdout.write('\033[4A')
