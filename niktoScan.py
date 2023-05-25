#!/usr/bin/env python3

import subprocess
import re
import os
import checkHosts
import resultsDir
import sharedData
# from sharedData import vulnerabilities

# global vulnerabilities
sharedData.vulnerabilities = f"\nNikto Results:\n"

def getScanResults():
	
	# Step 6: Perform nikto and check for vulnerabilities
	sharedData.vulnerabilities += f"\nPerforming Nikto Scan On Active Hosts\n"
	print("\nPerforming Nikto Scan On Active Hosts\n")
	counter=1

	for host in checkHosts.active_hosts:
	    print(str(counter)+". Nikto scan on "+host+". It could take upto 45 minutes for the scan to complete.\n")
	    try:
	    	nikto_output = subprocess.check_output(["nikto", "-h", host,"-ask", "no"]).decode()
	    except Exception as ex:
	    	sharedData.vulnerabilities+=f"\nAn Error Occured: {ex}\n"
	    	print(f"\nAn Error Occured: {ex}\n")
	    

	    sharedData.vulnerabilities +=f"\nNikto Findings for {host}\n"
	    # niktoFindings = ["Server:","clickjacking", "XSS", "vulnerable", "Wordpress", "leaks", "server", "nginx", "apache"]
	    for line in nikto_output.splitlines():

	        if any(finding in line for finding in sharedData.niktoFindings):
	            sharedData.vulnerabilities+=f"{line}\n"
	            print(line)
	    counter+=1

	sharedData.getSeparator(sharedData.results)
	print(sharedData.vulnerabilities)

	# Save vulnerabilities to a file
	sharedData.writeToFile(sharedData.getNiktoScanResultFile(),sharedData.vulnerabilities)