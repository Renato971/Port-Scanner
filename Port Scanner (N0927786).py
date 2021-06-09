from different_IP import *
import socket
import sys
import threading
import platform
import time
from datetime import datetime
from queue import Queue


class banner:
    # self = instance of class binds parameters to class
    def __init__(self, top_border, header, sub_header, bottom_border):
        # Welcome banner
        self.top_border = top_border  # defines the value from the class
        self.header = header
        self.sub_header = sub_header
        self.bottom_border = bottom_border


facts = banner("-" * 100, "                 The Multi-threaded Portscannator- 3000          ",
               "                       A project by Renato Dushku                    ", "-" * 100)

# prints the banner class
print(facts.top_border)  # prints the value of the class
print(facts.header)
print(facts.sub_header)
print(facts.bottom_border)

while True:
    username = input("Please enter your username:  ")
    if username == "Renato" and "Bob":  # sets a value for the username
        file = open("credentials.txt", "w")  # writes the username on the text file
        file.write("Renato" or "Bob""\n")
        file.close()
    else:
        var = username != "Renato" or "Bob"  # if value is incorrect
        print("Incorrect username, please try again")

    password = input("Please enter your password:  ")
    if password == "Dushku":  # sets a value for the password
        file = open("credentials.txt", "w")  # writes password on the text file
        file.write(password + "\n")
        file.close()
    else:
        var = password != "Dushku"  # if value is incorrect
        print("Wrong password")

    if username == "Renato" and password == "Dushku":
        file = open("credentials.txt", "r")  # reads values from text file
        print(hash(file.read()))  # hashes the password
        file.close()  # file is closed
        break  # loop ends when criteria is met
print("Welcome", username)
file = open("ext.txt", "w")  # opens another text file
file.write("We hope you are satisfied with our services")  # writes message to file
file.close()  # file is closed
file = open("ext.txt", "r")  # opens and reads message within this text file
print(file.read())
file.close()  # closes the file
file = open("credentials.txt", "a")  # opens text file and appends below print
question = "Have Fun!"  # adds a value
file.write(question + "\n")
file.write("ext.txt")
file.close()


def main():
    socket.setdefaulttimeout(0.30)  # sets a time to stop waiting for the socket
    print_lock = threading.Lock()  # the threading helps the ports to synchronise
    discovered_ports = []  # list for the ports taken from the IP
    if len(sys.argv) > 1:  # sys.argv is a list that collects all command-line arguments
        for remote_host in sys.argv[1:]:  # determine local host ip by outgoing test to another host

            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:  # within the brackets is a referral to the IPV4
                s.connect((remote_host, 9))  # Network in which the device is connected
                my_ip = s.getsockname()[0]  # gets the Host name of the device that the scan is running on
                print(my_ip, flush=True)  # prints IP of the device based on the Network connected is flushed to the
                # right destination

    else:
        time.sleep(1)  # time which started
        my_name = platform.node()  # saves IP as a variable
        my_ip = socket.gethostbyname(my_name)  # saves host name as variable
        print(my_ip)
    Host_Name = socket.gethostname()  # gets the host name of the target
    error = str("Invalid Input")  # if the input is not recognised

    try:
        target_ip = socket.gethostbyname(my_ip)  # gets the target
        print("-" * 100)
        print("Scanning IP: " + target_ip)  # displays the IP of the targeted host
        print("Host Name: " + Host_Name)  # prints the host name of the target device
        print("Time started scanning: " + str(datetime.now()))  # shows the date and time the scan started
        print("-" * 100)
        t1 = datetime.now()  # the current date and time
    except (UnboundLocalError, socket.gaierror):
        print(error)  # prints error message if invalid input
        sys.exit()  # stops the program

    def portscan(port):

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # the "s" variable refers to the IPV4 family

        try:
            s.bind((target_ip, port))  # joins socket with address
            with print_lock:
                discovered_ports.append(str(port))  # adds the discovered ports
            port.close()  # ends

        except (ConnectionRefusedError, AttributeError, OSError):  # errors such as client cannot connect to the port
            # on the computer running server, attribute assignment fails and system-related error are excepted
            print('Port open :', port, "\n")  # shows which port are open
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
        t.daemon = True  # runs without blocking program from exiting and when it ends the threads are closed too
        t.start()  # threading starts

    for worker in range(1, 200):  # range of ports to be scanned
        q.put(worker)

    q.join()  # if deleted code breaks; it joins the code below with the above one

    t2 = datetime.now()  # current time
    total = t2 - t1  # time taken workout
    print("Port scan completed in " + str(total))  # time of completion
    print("-" * 100)

    def automate():

        choice = '0'
        while choice == '0':
            print("Would you like to scan a different IP address, repeat the same scan, scan multiple IP's on a Network"
                  "or quit to terminal?")
            print("-" * 100)
            print("1 = Scan new IP address")  # scan a preferred IP (user input)
            print("2 = Repeat same port scan")  # run a port scan again
            print("3 = Scan multiple IP's on a Network")
            print("4 = Exit to terminal")  # end
            print("-" * 100)
            choice = input("Option Selection: ")  # user choice
            if choice == '1':
                print(choice_1())  # prints choice_1 from the other file

            elif choice == "2":
                main()  # goes back to the main to repeat all code again

            elif choice == "3":
                ip1 = input("enter IP1:  ")
                ip2 = input("enter IP2:  ")

                octet0 = int(ip1.split(".")[0])
                octet1 = int(ip1.split(".")[1])
                octet2 = int(ip1.split(".")[2])
                octet3 = int(ip1.split(".")[3])

                # convert ip1  to decimal
                ip1TODec = octet0 * (2 ** 24) + octet1 * (2 ** 16) + octet2 * (2 ** 8) + octet3  # is displays the
                # octate of the IP (8,8,8,8) (8+8+8+8)

                octet0 = int(ip2.split(".")[0])
                octet1 = int(ip2.split(".")[1])
                octet2 = int(ip2.split(".")[2])
                octet3 = int(ip2.split(".")[3])
                # convert ip2 to decimal
                ip2TODec = octet0 * (2 ** 24) + octet1 * (2 ** 16) + octet2 * (2 ** 8) + octet3

                total = abs(ip2TODec - ip1TODec) - 1
                print("Address available between Ip1 and IP2= ", total)

                def porttry(total, port):
                    try:
                        s.connect((total, port))  # connect the IP ranges to port
                        return True
                    except:
                        return None

                # calls porttry to check if that port is open
                for port in range(0, 200):
                    value = porttry(total, port)  # scants the ports of the IP range
                    if value is None:
                        print("Port not opened on %d" % port)
                    else:
                        print("Port opened on %d" % port)
                        break

            elif choice == "4":
                file = open("bye_message.txt", "r")  # reads text file
                message = file.read()  # saves the text file as a variable
                print(message)  # bob is summoned/ prints the text file
                file.close()  # closes text file
                sys.exit()  # exits the code/ finishes

            else:
                print("Please make a valid selection")
                automate()  # closes the loop if invalid input

    automate()  # closes the loop after it was run, if deleted automate will not run


# if deleted the code does not run
if __name__ == '__main__':
    try:
        main()  # goes back to main if its True
    except KeyboardInterrupt:
        print("\nGoodbye!")
        quit()  # end
