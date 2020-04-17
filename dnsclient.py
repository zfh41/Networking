#Name:Zaafira Hasan
#UCID: zfh4
#Section: CS 356-003


#! /usr/bin/env python3
# Echo Client
import sys
import socket
import random
import struct

# Get the server hostname, port and data length as command line arguments
host = sys.argv[1]
port = int(sys.argv[2])
hostname = sys.argv[3]

# Create UDP client socket. Note the use of SOCK_DGRAM
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientsocket.settimeout(1.0)

# Send data to server
# Receive the server response

msg_type = 1
retCode = 0
msgID = random.randint(1,100)
Qsection = hostname
qstLength = len(Qsection.encode('utf-8'))
ansLength = 0


print(Qsection.encode())
data = struct.pack("!HHIHH", msg_type, retCode, msgID, qstLength, ansLength)
sData = Qsection.encode()

data += sData
print(data)

for i in range(3):
    print("Sending Request to   " + host + ", " + str(port) + ": ")
    print("Message ID:    " + str(msgID))
    print("Question Length:    " + str(qstLength) + "  bytes")
    print("Answer Length:    "  + str(ansLength) + "  bytes" )
    print("Question:   " + Qsection)
    print("\n" + "\n")
    
    try:
        clientsocket.sendto(data,(host, port))
        dataEcho, address = clientsocket.recvfrom(1024)
        
        msg_type, retCode, msgID, qstLength, ansLength = struct.unpack("!HHIHH", dataEcho[:12])
        
        Qsection = dataEcho[12:12+qstLength]
        answer = dataEcho[12+qstLength:12+qstLength+ansLength]
        
        
        print("Received response from " + str(host) + ", " + str(port) + ":" )
        if retCode == 0:
            print("Return Code:  " + str(retCode) + " (No errors )")
        else:
            print("Return Code:  " + str(retCode) + " (Name does not exist )")
        print("Message ID:  " + str(msgID))
        print("Question Length: " + str(qstLength) + "  bytes")
        print("Answer Length:  " + str(ansLength) + "  bytes")
        print("Question:  " + Qsection.decode())
        if retCode == 0:
            print("Answer: " + answer.decode())
        
        break
    except socket.timeout:
        print("Request timed out ...")
        if i == 2:
            print("Request timed out ...  Exiting Program")




clientsocket.settimeout(None)
#Close the client socket
clientsocket.close()

