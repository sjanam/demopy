import socket, time

s = socket.socket()

host = socket.gethostname()

s.bind((host, 9999))
print('connected to' + host)

s.listen(4)
print('Server is listening......')
time.sleep(1)

while True:
    c1, address1 = s.accept()
    print('Connected to', address1)

    name = c1.recv(1024).decode()

    filename = 'EIS assignment.txt'
    f = open(filename, 'rb')
    l = f.read(1024)

    while (l):
        c1.send(l)
        l = f.read(1024)
    f.close()
    print('Done sending')

    c1.close()
