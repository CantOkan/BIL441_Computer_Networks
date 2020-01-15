
import socket
import time
import pickle
import cv2



HEADERIZE=10

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind((socket.gethostname(),2341))
s.listen(5)

connection=s.makefile('wb')

cam=cv2.VideoCapture(0)

cam.set(3,320)
cam.set(4,240)

img_counter=0
encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]

def send_data():
    ret, frame = cam.read()
    result, frame = cv2.imencode('.jpg', frame, encode_param)
    clientsocket,addr=s.accept()

    print(f'Connection from {addr} has been established!')
    d={1:"Hey",2:"There",3:frame}
    mymsg=pickle.dumps(d)

    msg=bytes(f'{len(mymsg):<{HEADERIZE}}','utf-8')+mymsg

    print("Giden msg",msg)
    clientsocket.send(msg)
    clientsocket.close()
    cam.release()

send_data()

send_data()