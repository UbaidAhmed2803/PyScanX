import sys

ip_list = []

def getHosts():
    global ip_list
    ip_list = input("Enter the list of Hosts (separated by spaces): ").split()


if __name__ == "__main__":
    getHosts()
    print("IP List:", ip_list)
    sys.exit()
