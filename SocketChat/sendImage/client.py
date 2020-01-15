import socket
import time
import pickle
import cv2

from threading import Thread

HEADERIZE=10


s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((socket.gethostname(),2341))

def read_msg():  
    full_msg=b''
    new_msg=True

    while True:
        msg=s.recv(1000)
        if new_msg:
            print(f"The len of the message={msg[:HEADERIZE]}")
            msglen=int(msg[:HEADERIZE])
            new_msg=False
        

        full_msg+=msg


        if(len(full_msg)-HEADERIZE==msglen):
            print("full msg recvd")
            print(full_msg[HEADERIZE:])

            d=pickle.loads(full_msg[HEADERIZE:])
            print("Pickled:",d)

            data=d[3]
            frame=cv2.imdecode(data,cv2.IMREAD_COLOR)
            cv2.imshow('Image',frame)
            cv2.waitKey(0)

            print("image:",data)
            new_msg=True

            full_msg=b''
            break
    

    print("last:",full_msg)



t1=Thread(target=read_msg)
t1.start()
client_socket.close()