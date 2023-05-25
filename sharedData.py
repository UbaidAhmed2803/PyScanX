import os
import re
from datetime import datetime

# Initialize variables to store results and vulnerabilities
results = ""
vulnerabilities = ""

# Get the current date and time
current_date = datetime.now()

# Initialize variables for directory name and scan number
newDirName = ""
newScanNumber = 0

# Specify the result directory and directory prefix
resultDirectory = "Results"
dirPrefix = "MyScan"
dirPath = os.path.join(resultDirectory, newDirName)

# Format the current date as "day_month_year"
dateOfScan = current_date.strftime("%d_%b_%Y")

# Common Nikto vulnerabilities keywords
niktoFindings = ["Server:","clickjacking", "XSS", "vulnerable", "Wordpress", "leaks", "server", "nginx", "apache","osvdb","missing","found","httponly","x-powered-by"]

#nmap ports



# Define file paths for storing results of different scans
activeInactiveHostsFile = "activeInactiveHosts.txt"
nmapResultFile = "nmapResults.txt"
sslScanResultFile = "sslScanResults.txt"
niktoScanResultFile = "niktoScanResultFile.txt"


def writeToFile(fileLocation,vulnerabilities):
	# Regular expression pattern to match ANSI escape codes
	escapeCodePattern = r"\033\[[0-9;]*m"
	escapeCode = re.findall(escapeCodePattern, vulnerabilities)
	textOnlyData = re.sub(escapeCodePattern, "",vulnerabilities)

	with open(fileLocation, "w") as file:
		file.write(textOnlyData)
	file.close()


def getHostStatusFile():
	return os.path.join(dirPath,activeInactiveHostsFile)

def getNmapResultFile():
	return os.path.join(dirPath,nmapResultFile)

def getSSLScanResultFile():
	return os.path.join(dirPath,sslScanResultFile)

def getNiktoScanResultFile():
	return os.path.join(dirPath,niktoScanResultFile)


def getSeparator(resultFile):
	i=20
	resultFile+=f"\n\t\t\t"
	print("\n")
	while i>0:
		print("*",end ='')
		resultFile+=f"*"
		i-=1
	print("\n")

	