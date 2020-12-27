import socket
import threading


server = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM,
)

server.bind(
    ("127.0.0.1", 228)
)

server.listen(5)
users = list()
print('Server is listening')


def send_all(data, current_user=None):
    for user in users:
        if user != current_user:
            user.send(data)



def listen_user(user):
    while True:
        data = user.recv(2048)
        send_all(data, current_user=user)


def start_server():
    while True:
        user_socket, adress = server.accept()
        

        print(f"User {user_socket} connected")
        
        users.append(user_socket)
        listen_accepted_user = threading.Thread(
            target=listen_user, 
            args=(user_socket,)
            )

        listen_accepted_user.start()
        # data = user_socket.recv(2048)

        # print(data.decode('utf-8'))

if __name__ == "__main__":
    start_server()