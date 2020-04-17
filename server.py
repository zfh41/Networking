#Name:Zaafira Hasan
#UCID: zfh4
#Section: CS 356-003


#! /usr/bin/env python3
# Echo Server
import sys
import socket
import random
import time
import struct
import re

# Read server IP address and port from command-line arguments
serverIP = sys.argv[1]
serverPort = int(sys.argv[2])

# Create a UDP socket. Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Assign server IP address and port number to socket
serverSocket.bind((serverIP, serverPort))




print("The server is ready to receive on port:  " + str(serverPort) + "\n")

# loop forever listening for incoming UDP messages
while True:
    
    # Generates a random number to ignore client ping
    
    sequenceNum, address = serverSocket.recvfrom(1024)
    
    ignoreInt = random.randint(0,10)
    msg_type = 2
    omsg_type, seqNum = struct.unpack("!II", sequenceNum)
    servTest = struct.pack("!II", msg_type, seqNum)
    num = re.sub('[(),]', '', str(seqNum))
    if(ignoreInt < 4):
        print("Message with sequence number " + num + " dropped" )

    else:
        print("Responding to ping request with sequence number " + num)
        serverSocket.sendto(servTest, address)
        
    # Receive and print the client data from "data" socket
    
    
    
    # Echo back to client
    
    

    
    
    
