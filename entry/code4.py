# WhoIsTool - Query and Response Protocol - Used for querying larged based databases (like ip addresses and domain names)

import socket # low level functionality for core networking services (HTTP and HTTPS request etc.)

def whois_lookup(domain: str): 
    s = socket.socket(socket.AF_INET, # variable s made, AFI_INET (Address Family Internet)
                      socket.SOCK_STREAM) # SOCKET_STREAM : We want to TCP a socket type - make a TCP request 
    s.connect(("whois.iana.org", 43)) # declared in variable s, use connect functionality of the socket library to connect to the URL given "whois.iana.org" on port 43
    s.send(f"{domain}\r\n".encode()) # send a request (a query) and encode it in a byte of strings
    response = s.recv(4096).decode() # responsible for receiving a response from the WhoIs server - buffer of 4096 - decode into a string
    s.close() # close the socket
    return response # return the response

print(whois_lookup("google.com")) # print the response if received and takes the argument "google.com"

# After running the script. Output: Information on google.com

# - When it is registered
# - When a domain is expired
# - When its client transferred (active) - locks down a domain to prevent access without permission 
# - Name server information (DNS servers)
# - etc.