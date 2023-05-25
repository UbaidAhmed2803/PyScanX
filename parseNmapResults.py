import re
import sharedData

def getResults(nmapOutput):
# Regular expression patterns to extract port and service information
	port_pattern = r"(\d+)/\w+\s+open"
	service_pattern = r"open\s+(\S+)\s+"

	# Extract port and service information using regular expressions
	ports = re.findall(port_pattern, nmapOutput)
	services = re.findall(service_pattern, nmapOutput)

	# Verify if the number of ports matches the number of services
	if len(ports) != len(services):
		print("Error: Mismatch in the number of ports and services.")
		return

    # Write the information to the output file in a tabular format
	
	sharedData.results+=f"\nPort\tService\n"
	sharedData.results+=f"====\t=======\n"

	for port, service in zip(ports, services):
		sharedData.results+=f"{port}\t{service}\n"
        

	return sharedData.results
	
	# with open(output_file, "w") as file:
    # 	file.write("Port\tService\n")
    # 	file.write("====\t=======\n")
    # 	for port, service in zip(ports, services):
    #     	file.write(f"{port}\t{service}\n")