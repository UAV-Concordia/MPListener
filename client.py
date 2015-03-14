'''
== APM Client ==
Test client to query APM flight data service
This test make a request to the server and print the response

The response must match the format described in server.py

This script is meant as test
'''
import struct
import socket

# Server configuration 
Service = (socket.gethostname(), 49000)

def main():
    sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sk.connect(Service)
    sk.send("GET")
    data = sk.recv(512)
    print struct.unpack("fff",data)
    sk.close()
    
if __name__ == "__main__":
    main()
