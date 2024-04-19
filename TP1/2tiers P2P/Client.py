import socket

class P2PClient:
    def send_request(self, host, port, request):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((host, port))
            sock.sendall(request.encode("utf-8"))
            response = sock.recv(1024).decode("utf-8")
        return response

if __name__ == "__main__":
    client = P2PClient()
    host = input("Enter server host: ")
    port = int(input("Enter server port: "))
    while True:
        request = input("Enter command (ADD/REMOVE/DISPLAY): ")
        if request.upper() in ("ADD", "REMOVE", "DISPLAY"):
            response = client.send_request(host, port, request.upper())
            print("Response:", response)
        else:
            print("Invalid command. Please enter ADD, REMOVE, or DISPLAY.")
