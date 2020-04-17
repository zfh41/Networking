#Name:Zaafira Hasan
#UCID: zfh4
#Section: CS 356-003


#! /usr/bin/env python3
# Echo Client
import sys
import socket
import struct
import time
import statistics
# Get the server hostname, port and data length as command line arguments
host = sys.argv[1]
port = int(sys.argv[2])


# Create UDP client socket. Note the use of SOCK_DGRAM
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


clientsocket.settimeout(1.0)

# Send data to server
# Receive the server response

print("Pinging   " + host + ", " + str(port))
seqNum = 0
loss = 0
recieve = 0
RTTList = []
for i in range(10):
    seqNum+=1
    msg_type = 1
    test = struct.pack("!II", msg_type, seqNum)
    
    try:
        clientsocket.sendto(test, (host, port))
        t1 = time.time()
        t2, address = clientsocket.recvfrom(1024)
        t2 = time.time()
        diff = t2-t1
        RTT = '%.6f'%(diff)
        RTTList.append(RTT)
        print("Ping message number " + str(seqNum) + " RTT: " + RTT + " secs")
        recieve +=1
        
    except socket.timeout:
        print("Ping message number " + str(seqNum) + " timed out")
        loss+=1

print("--------------------------------------")

print("Number of packets sent: 10" )
print("Number of packets received: " + str(recieve))
print("Number of packets lost: " + str(loss))
print("Percent Loss: ", "{0:.0%}".format(loss/10))

for i in range(0, len(RTTList)):
    RTTList[i] = float(RTTList[i])

avg = statistics.mean(RTTList)
avgRTT = '%.6f'%(avg)


print("Min RTT: " + str(min(RTTList)))
print("Max RTT: " + str(max(RTTList)))
print("Average RTT: " + str(avgRTT))



clientsocket.settimeout(None)
#Close the client socket
clientsocket.close()
