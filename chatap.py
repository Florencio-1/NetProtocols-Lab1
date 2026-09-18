import socket
import threading
import sys

connections = {}
connection_counter = 1

def handle_incoming_messages(conn, addr):
    while True:
        try:
            data = conn.recv(1024)
            if not data:
                break
            message = data.decode()
            print(f"\nMessage received from {addr[0]}\nSender's Port: {addr[1]}\nMessage: \"{message}\"\n> ", end="")
        except:
            break

def server_listening_thread(listen_port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("", listen_port))
    s.listen(10)

    while True:
        conn, addr = s.accept()
        thread = threading.Thread(target=handle_incoming_messages, args=(conn, addr))
        thread.start()

def main():
    if len(sys.argv) != 2:
        print("Use: python3 chatap.py <port>")
        sys.exit(1)

    my_port = int(sys.argv[1])

    listener_thread = threading.Thread(target=server_listening_thread, args=(my_port,), daemon=True)
    listener_thread.start()

    # Main Loop
    while True:
        command_input = input("> ").strip().split()
        if not command_input:
            continue

        command = command_input[0].lower()

        if command == "help":
            print("Commands: help, myip, myport, connect, list, terminate, send, exit")
        elif command == "myip":
            pass 
        elif command == "myport":
            print(f"Listening on port: {my_port}")
        elif command == "connect":
            pass
        elif command == "list":
            pass
        elif command == "terminate":
            pass 
        elif command == "send":
            pass 
        elif command == "exit":
            break
        else:
            print("Unknown command. Type 'help' for options.")

if __name__ == "__main__":
    main()
