import socket
from threading import Thread

import tkinter as tk
from tkinter import *

window=Tk()
window.title("Client:Alperen Köylü")
canvas=Canvas(window,width=500,height=500)
canvas.pack()

port=1234
client_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#client_socket.connect(("localhost",1234))

#127.0.1.1
client_socket.connect(("localhost",port))


def receive_data():
    while True:
        data=client_socket.recv(1000)
        data=data.decode()
        print("\n Server send:",data)
        listbox.insert(tk.END,"Server:"+data)


def sending_data():
    msg=str(textbox.get())
    userinput=msg.encode()
    client_socket.sendall(userinput)


t1=Thread(target=receive_data)
t1.start()
       

while(True):
    listbox = Listbox(window,width=50, height=20)
    listbox.place(x=80,y=120)
    lbl1=Label(window,text="Enter your message",font=("arial",20)).place(x=20,y=20)
    textbox=StringVar()
    entry_box=Entry(window,textvariable=textbox,width=50).place(x=20,y=60)
    work=Button(window,text="Send",width=4,height=1,command=sending_data).place(x=20,y=90)
    window.mainloop()



