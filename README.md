
# BIL441_Computer_Networks
## Computer networks lecture's projects

## 1. Socket Programming
#### Socket prog. is a way of connecting two nodes. We've a Server and Client in a project and they bind each other with statically given IP. Before go further, You have to know IP add. of the other devices. 

![Scoket](https://user-images.githubusercontent.com/25572428/72451518-19dda180-37cd-11ea-9f82-75789dff3258.PNG)


## 2. Reliable Data Transfer Protocols
#### For connection-oriented service provided by TCP, it is necessary to have a reliable data transfer (RDT) protocol to ensure delivery of all packets and to enable the receiver to deliver the packets in order to its application layer. This protocol is also known as a stop-and-wait protocol: after sending each packet the sender stops and waits for feedback from the receiver indicating that the packet has been received .

#### This project is a simply implementation(simulation) of RDT Protocols.

##### RDT 1.0 : There is no packet loss and bit errors in channel.
##### RDT 2.0 : There is no packet loss but It can occurs bit errors in channel.
##### RDT 2.1 : In addition to all, Seq # is added and bit error can happens for ACK AND NACK
##### RDT 2.2 : All assumption same with Rdt 2.1 but there is no more NACK. We integrate the Timer instead of Nack .
##### RDT 3.0 : In this protocol channel is not  %100 safe so that Packet loss can occur, and also bit error frequently happens in a packet transmitting .

## As I mentioned that is the simply implementation of RDT protocols. There are many assumption and disregarded things in projects.
