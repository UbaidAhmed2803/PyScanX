#!/usr/bin/env python3

import subprocess
import re
import os
import userInput
import checkHosts
import sharedData
import resultsDir
# from sharedData import results
from sharedData import vulnerabilities
import nmapScan
import sslScan
import niktoScan

# global vulnerabilities



userInput.getHosts()
resultsDir.getCount()
# ip_list = input("Enter the list of IPs (separated by spaces): ").split()

# Step 2: Perform Nmap scan to check active hosts

checkHosts.getActiveHosts()
# results  = "**********Scan Results**********\n"+sharedData.results
# print(results)

nmapScan.getScanResults()

# active_hosts =[]
# inactive_hosts = []
# Step 3: Perform Nmap scan on active hosts to check open ports and services

# scan_results = ""

# print(scanResultsCount.newScanNumber)

# nmapScan.getScanResults()

sslScan.getScanResults()



# Step 5: Perform sslscan and check for vulnerabilities
   
# file.close()

niktoScan.getScanResults()

print("Scan and vulnerability check completed. Results saved under "+sharedData.dirPath+".")
