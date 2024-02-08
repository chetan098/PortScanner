import socket
import threading
print("Port Scanner made by Chetan Pujari");
target_host = input("Enter the domain name: ")
target_ports = [
    7, 20, 21, 22, 23, 25, 53, 69, 80, 88, 102, 110, 135, 137, 139, 143, 381, 383, 443, 464,
    465, 587, 593, 636, 691, 902, 989, 990, 993, 995, 1025, 1194, 1337, 1589, 1725, 2082,
    2083, 2483, 2484, 2967, 3074, 3306, 3724, 4664, 5432, 5900, 6665, 6669, 6881, 6999, 6970,
    8086, 8087, 8222, 9100, 10000, 12345, 27374, 18006, 27017, 28017, 50000
]

def scan_port(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target_host, port))
        if result == 0:
            print(f"\033[92mPort {port} is open\033[0m")
        else:
            print(f"\033[91mPort {port} is closed\033[0m")
        sock.close()
    except Exception as e:
        print(f"Error: {e}")

def main():
    print(f"Scanning host {target_host}...")
    threads = []
    for port in target_ports:
        thread = threading.Thread(target=scan_port, args=(port,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
