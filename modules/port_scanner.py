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

    open_ports = []
    error_count = 0

    for port in range(start, end + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(0.5)
            try:
                result = sock.connect_ex((host, port))
                if result == 0:
                    print(Fore.GREEN + f"Port {port} open")
                    open_ports.append(port)
            except socket.gaierror:
                print(Fore.RED + f"Hostname could not be resolved for port {port}")
                error_count += 1
            except socket.error as e:
                print(Fore.RED + f"Couldn't connect to server on port {port}: {e}")
                error_count += 1

    print(Fore.CYAN + "Scan complete.")
    print(f"Open ports: {len(open_ports)}")
    if error_count:
        print(Fore.RED + f"Errors: {error_count}")

