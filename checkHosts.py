#!/usr/bin/env python3

import subprocess
import re
import os
import userInput
import sharedData
import resultsDir
import sys


#Checking Active & Inactive Hosts

active_hosts = []
inactive_hosts = []

def getActiveHosts():
    print("Checking for active & inactive hosts:\n")
    global active_hosts, inactive_hosts
    counter = 1

    hosts_status = f"Hosts' Status\n"
    for ip in userInput.ip_list:
        nmap_output = subprocess.check_output(["nmap", "-sn", ip]).decode()
        # nmap_output =subprocess.run(["nmap", "-sn", ip], capture_output=True, text=True)
        if "Host is up" in nmap_output:
            active_hosts.append(ip)
            hosts_status=f"{hosts_status}\n{counter}. {ip} [ACTIVE]."
            print(str(counter)+". "+ip+" [ACTIVE]")
            counter+=1
        else:
            inactive_hosts.append(ip)
            hosts_status=f"{hosts_status}\n{counter}. {ip} [INACTIVE]."
            print(str(counter)+". "+ip+" [INACTIVE]")
            counter+=1

        sharedData.results=f"{hosts_status}\n"    

    # with open(sharedData.getHostStatusFile(), "w") as file:
    #     file.write(hosts_status)
    if(len(active_hosts)==0):
        print("No Active Hosts")
        # break;end
        sys.exit()

    sharedData.getSeparator(sharedData.results)
    sharedData.writeToFile(sharedData.getHostStatusFile(),hosts_status)

if __name__ == "__main__":
    getActiveHosts()
    print("Active Hosts:", active_hosts)
    print("Inactive Hosts:", inactive_hosts)