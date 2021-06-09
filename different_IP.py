import socket
import sys
import threading
import time
from datetime import datetime
from queue import Queue


def choice_1():
    time.sleep(1)
    target = input("Enter your target IP address or a URL to scan: ")  # interactive port search (website/ IP)
    Host_Name = socket.gethostname()  # gets the host name of the target
    error = str("Invalid Input")  # if the input is not recognised

    try:
        target_ip = socket.gethostbyname(target)  # gets the target
        print("-" * 100)
        print("Scanning IP: " + target_ip)  # displays the IP of the targeted host
        print("Host Name: " + Host_Name)  # prints the host name of the target device
        print("Time started scanning: " + str(datetime.now()))  # shows the date and time the scan started
        print("-" * 100)
        t1 = datetime.now()  # the current date and time

    except (UnboundLocalError, socket.gaierror):
        print(error)  # prints error message if invalid input
        sys.exit()  # stops the program

    def portscan(port, print_lock=None, discovered_ports=None):  # create a parameter for print_lock and discovered_ports

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            s.bind((target_ip, port))  # joins socket with address
            with print_lock:
                discovered_ports.append(str(port))  # adds ports
            port.close()

        except (ConnectionRefusedError, AttributeError, OSError):
            print('Port open :', port, "\n")  # shows which port is open
            pass

    def threader():
        while True:
            worker = q.get()  # gets the ports
            portscan(worker)  # scans the ports
            q.task_done()  # port is scanned

    q = Queue()  # puts the ports in a queue

    # if deleted it wont print the ports
    for x in range(200):
        t = threading.Thread(target=threader)  # threads the target
        t.daemon = True
        t.start()  # threading starts

    for worker in range(1, 200):  # range of ports to be scanned
        q.put(worker)

    q.join()  # if deleted code breaks; it joins the code below with the above one

    t2 = datetime.now()  # current time
    total = t2 - t1  # time taken workout
    print("Port scan completed in " + str(total))  # time of completion
    print("-" * 100)
