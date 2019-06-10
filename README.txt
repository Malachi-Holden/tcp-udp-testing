Malachi Holden
Final project
Testing the Speed of UDP transmission

Problem statement:

My project is to test the transmission speed of UDP and TCP communication between two computers over Ethernet. I will write server and client software on the respective computers, as well as timing/performance measuring software to test the transmission time. This will be done on a Dell XPS 15 running Ubuntu 18.04, and a Dell Lattitude E6440 running Windows 7. I will test the client software on the XPS and the server on the Lattitude, with both UDP and TCP, and I will compare the speeds.

Background:
The idea for this project originates from a paper called "Performance of UDP and TCP
Communication on Personal Computers" by Andro Milanović, Siniša Srbljić, and Vlado Sruk.
The main advantage of using UDP is its speed -- or at least, this is what we have been told. Therefore I wanted to build a project to measure the speed of UDP communications with various message sizes.

How does it compare to TCP?


Description of program:
The program has two files: server.py and client.py, to be run on the server and client respectively. Each uses the python socket module to send and recieve UDP transmissions. The idea is for the client computer to create a socket, record a timestamp, and send a UDP message to a server. The server also records a timestamp, saving the time that it receives the UDP message. Then the server sends a response message back to the client containing the reception time. The client server, upon receiving the response, now has the sending and receiving time, and can now calculate the travel time.

To test whether message size affects the travel time, a series of tests can be run, sending messages of various sizes. This can be done using a for-loop and sending messages of size i, where i ranges according to the for-loop.

See the testing.txt file for the results of my research.



To run a UDP test:

choose a server computer and a client computer. On the server computer, edit the UDPserver.py file to change the class variable UDP_IP_ADDRESS to the server computer's ip address, and UDP_PORT_NO to a chosen port number on the server computer. Change outputfile to the filename of your choice.

Set followupaddress and followupport to the appropriate address and port of the client computer.

On the client computer, edit the UDPclient.py file to change the class variable SERVER_IP_ADDRESS and SERVER_PORT_NO to the server's address and port, and change FOLLOW_UP_ADDRESS and FOLLOW_UP_PORT to the client's address and port.

Now on the server computer, run UDPserver.py with python 3.

Next, on the client computer run UDPclient.py $n $m with python 3, where $n and $m are parameters. These are numbers from 1 to 1024, the upper and lower bound for the number of characters you wish to transmit in your test. So if you enter 3 and 6 as parameters, the program will send first 3 characters, then 4, then 5, and then 6.

Finally look in the directory containing the UDPclient.py file and see the file whose title you chose. This contains the desired transmission speeds. The client program also prints some useful information to the terminal, but not all of the speeds.

To run the TCP test, follow these exact instructions, adjusting as necessary, using the files TCPserver.py and TCPclient.py. Not as many addresses need to be entered at the top.






_____
