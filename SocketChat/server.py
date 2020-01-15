import socket
from threading import Thread
import tkinter as tk

from tkinter import *

window=Tk()
window.title("Server:CAN OKAN Taşkıran")
canvas=Canvas(window,width=500,height=500)
canvas.pack()


port=1234

server_socket=socket.socket()

server_socket.bind(("127.0.0.1",port))
#server_socket.bind(('',port))



server_socket.listen()

conn,addr=server_socket.accept()

print("Got a client from address",addr)

def receive_data():
    while True:
        data=conn.recv(1000)
        data=data.decode()
        print("\n received data:",data)
        listbox.insert(tk.END,str(addr)+":"+data)


def send_data():
    msg=str(textbox.get())
    userinput=msg.encode()
    conn.sendall(userinput)

t=Thread(target=receive_data)
t.start()

while True:
    listbox = Listbox(window,width=50, height=20)
    listbox.place(x=80,y=120)
    lbl1=Label(window,text="Enter your message",font=("arial",20)).place(x=20,y=20)
    textbox=StringVar()
    entry_box=Entry(window,textvariable=textbox,width=50).place(x=20,y=60)
    msg=str(textbox.get())
    work=Button(window,text="Send",width=4,height=1,command=send_data).place(x=20,y=90)
    window.mainloop()




server_socket.close()



