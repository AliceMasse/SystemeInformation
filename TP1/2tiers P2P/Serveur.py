import socket
import threading

class Book:
    def __init__(self, name, tag, image):
        self.name = name
        self.tag = tag
        self.image = image

    def __str__(self):
        return f'Book: {self.name} ({self.tag})'

class P2PServer:
    def __init__(self, port):
        self.port = port
        self.library = []

    def start(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(('localhost', self.port))
        server_socket.listen(5)
        print(f"P2P Server started on port {self.port}")

        while True:
            client_socket, _ = server_socket.accept()
            print("New connection accepted.")
            threading.Thread(target=self.handle_client, args=(client_socket,)).start()

    def handle_client(self, client_socket):
        data = client_socket.recv(1024).decode("utf-8")
        if not data:
            client_socket.close()
            return

        parts = data.split()
        if not parts:
            client_socket.sendall("Invalid command.".encode("utf-8"))
            client_socket.close()
            return

        action = parts[0]
        if action == "ADD":
            if len(parts) != 4:
                response = "Usage: ADD <name> <tag> <image>"
            else:
                name, tag, image = parts[1], parts[2], parts[3]
                book = Book(name, tag, image)
                self.library.append(book)
                response = f"Book '{name}' added to the library."
        elif action == "REMOVE":
            if len(parts) != 2:
                response = "Usage: REMOVE <name>"
            else:
                name = parts[1]
                found = False
                for book in self.library:
                    if book.name == name:
                        self.library.remove(book)
                        response = f"Book '{name}' removed from the library."
                        found = True
                        break
                if not found:
                    response = f"Book '{name}' not found in the library."
        elif action == "DISPLAY":
            if self.library:
                books_info = '\n'.join(str(book) for book in self.library)
                response = f'Books in the library:\n{books_info}'
            else:
                response = "The library is empty."
        else:
            response = "Unknown command."

        client_socket.sendall(response.encode("utf-8"))
        client_socket.close()

if __name__ == "__main__":
    server = P2PServer(9999)
    server.start()
