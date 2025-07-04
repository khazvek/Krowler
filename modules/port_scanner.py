"""Simple TCP Port Scanner"""

import socket
from colorama import Fore


def run():
    print(Fore.CYAN + "[Port Scanner]")
    print("Enter host and port range (e.g. 20-80)")
    host = input("Host: ")
    prange = input("Range start-end: ")
    try:
        start, end = [int(p) for p in prange.split('-')]
    except ValueError:
        print(Fore.RED + "Invalid range format")
        return

    print(Fore.YELLOW + f"Scanning {host} from {start} to {end}...")
    for port in range(start, end + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(0.5)
            try:
                result = sock.connect_ex((host, port))
                if result == 0:
                    print(Fore.GREEN + f"Port {port} open")
            except socket.gaierror:
                print(Fore.RED + "Hostname could not be resolved")
                break
            except socket.error:
                print(Fore.RED + "Couldn't connect to server")
                break
