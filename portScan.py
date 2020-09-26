def portScanner(fullip):
    import socket
#making list to store all open ports.
    openports=[]
    remoteServerIP  = socket.gethostbyname(fullip)
    for port in range(1,10000):  
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            openports.append(port)
        else :
            sock.close()
    return openports

