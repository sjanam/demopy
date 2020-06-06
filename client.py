import socket, time

c1 = socket.socket()
host = socket.gethostname()
host_name = input("Enter Ip address: ")
ip = socket.gethostbyname_ex(host)

c1.connect((host, 9999))
print('connected to', host)

c1.send(bytes('hello', 'utf-8'))

with open('received_file', 'wb') as f:
    print('file opened')

    while True:
        print('receiving data...')
        name = c1.recv(1024)
        print('data=%s', name)
        if not name:
            break
        # write data to a file
        f.write(name)

f.close()
c1.close()
