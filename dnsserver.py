#Name:Zaafira Hasan
#UCID: zfh4
#Section: CS 356-003


#! /usr/bin/env python3
# Echo Server
import sys
import socket
import struct
import difflib
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
    # Receive and print the client data from "data" socket
    data, address = serverSocket.recvfrom(1024)
    omsg_type, ortcode, msg_ID, qstLength, oaLngth = struct.unpack("!HHIHH", data[:12])
    qst = data[12:12+qstLength].decode()
    answer = ""
    with open('dns-master.txt') as f:
        for line in f:
            if qst in line:
                answer = line
                rtCode = 0
                break
            else:
                rtCode = 1
    ansLength = len(answer.encode('utf-8'))
    
    msg_type = 2
    
    data = struct.pack("!HHIHH", msg_type, rtCode, msg_ID, qstLength, ansLength)
    
    newq = qst.encode()
    
    ans = answer.encode()
    
    data = data + newq + ans
    
    
    # Echo back to client
    print("Sending data to client ")
    serverSocket.sendto(data,address)

