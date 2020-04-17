#Name: Zaafira Hasan
#UCID: zfh4
#Section: CS 356-003

#! /usr/bin/env python3
# http server

import sys
import socket
import os.path,time
from os import path
from datetime import datetime
import re

now = datetime.now()
dt_string=now.strftime("%a, %d %b %Y %H:%M:%S %Z")

host = sys.argv[1]
port = int(sys.argv[2])
dataLen = 1000000

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((host, port))
serverSocket.listen(1)
while True:
    connectionSocket, address = serverSocket.accept()
    data = connectionSocket.recv(dataLen)
    print(data.decode())
    
    unifRL = re.split('(\/)|( HTTP)|(Since: )|(\n)', data.decode())
    
    filename=unifRL[5]
    
    if (path.exists(filename)):
        if "If-Modified-Since" in data.decode():
            nmod=time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime(os.path.getmtime(filename)))
            unifRL = re.split('(\/)|( HTTP)|(Since: )|(\n)', data.decode())
            modified=unifRL[30]
            filename=unifRL[5]
            
            if (nmod in modified):
                shamh = "HTTP \/1.1 304 Not Modified\\r\\n"
                connectionSocket.send(shamh.encode())
            else:
                nmod=time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime(os.path.getmtime(filename)))
                with open(filename) as myfile:
                    head = [next(myfile) for x in range(3)]
                Modified = "HTTP/1.1  200  OK\r\n" + "Date: " + dt_string + "GMT\r\n" + "Last-Modified: " + nmod + " GMT\r\n" + "Content-Length:  " + str(os.stat(filename).st_size) +"\r\n"+"Content-Type: text/html; charset=UTF-8\r\n"+"\r\n"+head[0] + head[1] + head[2]
                print(Modified)
                connectionSocket.send(Modified.encode())
        else:
            nmod=time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime(os.path.getmtime(filename)))
            with open(filename) as myfile:
                head = [next(myfile) for x in range(3)]
            Modified = "HTTP/1.1  200  OK\r\n" + "Date: " + dt_string + "GMT\r\n" + "Last-Modified: " + nmod + " GMT\r\n" + "Content-Length:  " + str(os.stat(filename).st_size) +"\r\n" + "Content-Type: txt/html" + ";  charset=UTF-8\r\n" + "\r\n" + head[0] + head[1] + head[2]

            print(Modified)

            connectionSocket.send(Modified.encode())
            
    else:
         NotFound = "HTTP/1.1 404 Not Found\r\n" + "Date:" + dt_string + "GMT\r\n"  + "\r\n"
         print(NotFound)
         connectionSocket.send(NotFound.encode())
