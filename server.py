'''
== APM Service ==
Provide APM flight data

== PROTOCOL ==
BUFFER SIZE: 512B
REQ:
    any data
RES:
    Standardized float 4B for x86
    {   Altitude,
        Latitude,
        Longitude }
'''
import struct
import socket
import threading

# Server configuration 
Service = (socket.gethostname(), 49000)

# Data marshaller
def packData(cs):
    return struct.pack("fff", cs.alt, cs.lat, cs.lng)

# Notes
def printNotes():
    print """
    ******************************************
    Warning:
    By aborting this script the service socket will remain
    open. Therefore any subsequent execution of this
    script will fail.

    In order to close the hanging socket you need
    to shutdown this instance of the Mission Planner.
    ******************************************
    """

def main():
    try:
        sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        print "Binding socket at ", Service[0],":",Service[1]
        sk.bind(Service)
        print "MP Server ONLINE"
        while 1:
            msg, addr = sk.recvfrom(512)
            if(msg is "QUIT"):
                print "Connection close by remote"
                break
            data = packData(cs)
            #print "Request : ", msg
            #print "Response: ", data 
            sk.sendto(data, addr)
    except (KeyboardInterrupt, SystemExit, BaseException):
        pass
    finally:
        sk.close()
        print "MP Server OFFLINE"
    
# Script
printNotes()
main()
