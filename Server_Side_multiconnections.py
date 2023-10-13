import socket
import threading
import time
import string
import codecs

address = "localhost"
#ports:
tx_enb=2000
rx_enb=2009
tx_ue1=2010
rx_ue1=2008
tx_ue2=2007
rx_ue2=2006
#socks:
enb_tx_conn=0
enb_rx_conn=0
ue1_tx_conn=0
ue1_rx_conn=0
ue2_tx_conn=0
ue2_rx_conn=0
#messages
message_from_enb=''
message_from_ue=''

def send_to_gnb(conn):
    while True:
        last_message = message_from_ue
        byte_representation = codecs.encode(last_message)
        conn.sendall(byte_representation)
        while True:
            if (last_message != message_from_ue):
                break
        time.sleep(0.01)
        
def send_to_ue(conn):
    while True:
        last_message = message_from_enb
        byte_representation = codecs.encode(last_message)
        conn.sendall(byte_representation)
        while True:
            if (last_message != message_from_enb):
                break
        time.sleep(0.01)
        
def recv_from_enb(conn):
    global message_from_enb
    while True:
        message_from_enb = conn.recv(1024)
        print(message_from_enb)
        time.sleep(0.001)
        
def recv_from_ue(conn):
    global message_from_ue
    while True:
        message_from_ue = conn.recv(1024)
        print(message_from_ue)
        time.sleep(0.001)

def run_rx_client(port,type):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as listening_sock:
        print("rx_client ran1")
        ran = 0
        while True:
            if type =='tx' and enb_rx_conn != 0 and ran != 1:
                print("enb_rx_client ran")
                listening_sock.connect((address,port))
                print("Rx connection made")
                threading.Thread(target=recv_from_enb,args=(listening_sock,), daemon=True).start()
                ran = 1
            elif type =='tx1' and ue1_rx_conn != 0 and ran != 1:
                print("rue1_x_client ran")
                listening_sock.connect((address,port))
                print("Rx connection made")
                threading.Thread(target=recv_from_enb,args=(listening_sock,), daemon=True).start()
                ran = 1
            elif type =='tx2' and ue2_rx_conn != 0 and ran != 1:
                print("ue2_rx_client ran")
                listening_sock.connect((address,port))
                print("Rx connection made")
                threading.Thread(target=recv_from_enb,args=(listening_sock,), daemon=True).start()
                ran = 1
            else:
                time.sleep(5)

def run_tx_server(port, type):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as listening_sock:
        listening_sock.bind((address, port))
        listening_sock.listen()
        print("Listening function ran\n")
        if (type == 'rx'):
            #while True:
            global enb_rx_conn
            enb_rx_conn, client_address = listening_sock.accept()
            print("Tx connection made")
            threading.Thread(target=send_to_gnb,args=(enb_rx_conn,), daemon=True).start()
        elif (type == 'rx1'):
            #while True:
            global ue1_rx_conn
            ue1_rx_conn, client_address = listening_sock.accept()
            print("Tx connection made")
            threading.Thread(target=send_to_ue,args=(ue1_rx_conn,), daemon=True).start()
        elif (type == 'rx2'):
            #while True:
            global ue2_rx_conn
            ue2_rx_conn, client_address = listening_sock.accept()
            print("Tx connection made")
            threading.Thread(target=send_to_ue,args=(ue2_rx_conn,), daemon=True).start()

def enb(tx, rx):
    threading.Thread(target=run_tx_server,args=(rx, "rx",), daemon=True).start()
    threading.Thread(target=run_rx_client,args=(tx, "tx",), daemon=True).start()


def ue1(tx, rx):
    threading.Thread(target=run_tx_server,args=(rx, "rx1",), daemon=True).start()
    threading.Thread(target=run_rx_client,args=(tx, "tx1"), daemon=True).start()

def ue2(tx, rx):
    threading.Thread(target=run_tx_server,args=(rx, "rx2",), daemon=True).start()
    threading.Thread(target=run_rx_client,args=(tx, "tx2"), daemon=True).start()

def main():
    enb(tx_enb, rx_enb)
    ue1(tx_ue1, rx_ue1)
    ue2(tx_ue2, rx_ue2)
    time.sleep(1)
    x = input("Press Enter to exit: ")

main()
























































































































































































































































































































































































#Written by Oliver Higginbotham