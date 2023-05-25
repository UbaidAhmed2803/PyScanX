#!/usr/bin/env python3

import subprocess
import re
import os
import checkHosts
import resultsDir
import sharedData
from datetime import datetime

def getScanResults():
    counter=1
    print("\nPerforming SSLscan On Active Hosts\n")
    sharedData.vulnerabilities+=f"Performing SSLscan on Active Hosts:\n"
    for host in checkHosts.active_hosts:
        print("\n"+str(counter)+". " + host + " :\n")
        sharedData.vulnerabilities+=f"\n{counter}. {host} findings:\n\n"
        sslVulnerability=0
        try:
            sslscan_output = subprocess.check_output(["sslscan", host]).decode()
            
            print("SSLScan is done. Below are the findings:\n")
            heartbleed=['TLSv1.3 vulnerable to heartbleed','TLSv1.2 vulnerable to heartbleed','TLSv1.1 vulnerable to heartbleed']   
            tlsVulnerability="enabled"
            sslExpiryDate=""


            for line in sslscan_output.splitlines():
                if tlsVulnerability in line:
                    if ("TLSv1.1" or "TLSv1.0" or "TLSv1.2") in line:
                        sharedData.vulnerabilities+= f"{line}\n"
                        print(line.strip())
                        sslVulnerability+=1
            
                for issues in heartbleed:
                    if issues in line:
                        sharedData.vulnerabilities+= f"{line}\n"
                        print(issues) 
                        sslVulnerability+=1
                

                if "Not valid after:" in line:
                    sslExpiryDate=line[16:]     
        
            try:
                date_object = datetime.strptime(sslExpiryDate.strip(),"\x1b[31m%b %d %H:%M:%S %Y %Z\x1b[0m")
                sslVulnerability+=1
                sharedData.vulnerabilities+=f"SSL Expired on: "+sslExpiryDate.strip()+"\n"
            except Exception as e:
                date_object = datetime.strptime(sslExpiryDate.strip(),"\x1b[32m%b %d %H:%M:%S %Y %Z\x1b[0m")
                sharedData.vulnerabilities+=f"SSL Expires on: "+sslExpiryDate.strip()+"\n"
            

            if sslVulnerability==0:
                sharedData.vulnerabilities += f"\nNo vulnerabilities found via sslscan\n\n"    
            
        except Exception as ex:
            sharedData.vulnerabilities+=f"\n SSLscan failed on {host}. Certificate information cannot be retrieved.\n\n"
            print("SSLscan failed on "+host+". Certificate information cannot be retrieved.\n")

        counter+=1 
    
    sharedData.getSeparator(sharedData.vulnerabilities)
    print(sharedData.vulnerabilities)

    sharedData.writeToFile(sharedData.getSSLScanResultFile(),sharedData.vulnerabilities)  