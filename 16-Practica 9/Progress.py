from time import sleep
import netifaces as ni
import sys

print ("Loading, please wait...")
for i in range(21):
    sys.stdout.write('\r')
    # the exact output you're looking for:
    sys.stdout.write("[%-20s] %d%%" % ('='*i, 5*i))
    sys.stdout.flush()
    sleep(0.25)

print ("\nLoading, please wait...")
for i in range(21):
    sys.stdout.write('\r')
    # the exact output you're looking for:
    sys.stdout.write("[%-20s] %d%%" % ('='*i, 5*i))
    sys.stdout.flush()
    sleep(0.25)



    ni.ifaddresses('eth0')
    ip = ni.ifaddresses('eth0')[2][0]['addr']
    print (ip)  # should print "192.168.100.37"