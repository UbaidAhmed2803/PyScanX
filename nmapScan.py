#!/usr/bin/env python3

import subprocess
import re
import os
import checkHosts
import sharedData
import resultsDir
import parseNmapResults


def getScanResults():
	counter=1
	print("\nPerforming Nmap Scan On Active Hosts\n")
	sharedData.results+=f"\nPerforming Nmap Scan On Active Hosts:\n"

	for host in checkHosts.active_hosts:
		print("\n"+str(counter)+". " + host + " :\n")
		sharedData.results+=f"\n{counter}. {host}:\n"

		command=f"nmap -sV -A -p- {host}"
		
		try:
			nmapOutput = subprocess.check_output(["nmap", "-sV", "-p80,443","-T4", host]).decode()
		except Exception as ex:
			sharedData.results+=f"\nAn error occured: {ex}\n"
			print("\nAn error occured: {ex}\n")

		print(host+" Nmap scan DONE\n")
		# sharedData.results += f"\n{nmapOutput}\n"
		
		counter+=1

		parseNmapResults.getResults(nmapOutput)
		sharedData.getSeparator(sharedData.results)
		print(sharedData.results)
	
	sharedData.writeToFile(sharedData.getNmapResultFile(),sharedData.results)
