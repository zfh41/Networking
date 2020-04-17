#Name: Zaafira Hasan
#UCID: zfh4
#Section: CS 356-003

#! /usr/bin/env python3
# http client

import sys
import socket
import re
import struct
import os.path,time
from os import path

unifRL = sys.argv[1]

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
unifRL = re.split('[:\/]', unifRL)

host=unifRL[0]
port=int(unifRL[1])
cont=unifRL[2]

clientSocket.connect((host, port))

if os.path.exists("cache.txt"):
    append_write = 'a'
else:
    append_write = 'w'

l = open("cache.txt",append_write)

GetMsg = "GET  " + "/" + cont + " HTTP/1.1\r\n" + "Host:  " + host + ":" + str(port) + "\r\n" + "\r\n"

with open('cache.txt') as f:
    for line in f:
        if cont in line:
            place = re.split('.html|.txt', line)
            mod=place[1]
            conditionalGet="GET /"+cont+" HTTP/1.1\r\nHost:   "+str(host)+":"+str(port)+"\r\n"+"If-Modified-Since: "+mod+" GMT"+"\r\n"
            print(conditionalGet)
            clientSocket.send(conditionalGet.encode())
            dataEcho = clientSocket.recv(1024)
            print(dataEcho.decode())
        else:
            data=GetMsg
            print(data)
            clientSocket.send(data.encode())
            dataEcho = clientSocket.recv(1024)
            print(dataEcho.decode())
            if ("OK" in dataEcho.decode()):
                unifRL = re.split('(\/)|( HTTP)|(Since: )|(\n)|(: )|( GMT)', dataEcho.decode())
                modtime=unifRL[42]+" GMT"
                l=open("cache.txt","w+")
                l.write(cont+" "+modtime+ " GMT\n")
                l.close()
    
    if(os.stat("cache.txt").st_size == 0):
        data=GetMsg
        print(data)
        clientSocket.send(data.encode())
        dataEcho = clientSocket.recv(1024)
        print(dataEcho.decode())
        
        if ("OK" in dataEcho.decode()):
           unifRL = re.split('(\/)|( HTTP)|(Since: )|(\n)|(: )|( GMT)', dataEcho.decode())
           modtime=unifRL[42]
           l.write(cont+" "+modtime+ " GMT\n")
           l.close()
           clientSocket.close()

f.close()
