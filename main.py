import sys
from colorama import init, Fore
from pyfiglet import figlet_format

from modules import (
    whois_lookup,
    dns_lookup,
    ip_tracker,
    port_scanner,
    github_user_scanner,
)

init(autoreset=True)


def banner():
    print(Fore.CYAN + figlet_format("KRAKEN TOOL", font="slant"))


def menu():
    print(Fore.GREEN + "1. Whois Lookup")
    print(Fore.GREEN + "2. DNS Lookup")
    print(Fore.GREEN + "3. IP Tracker")
    print(Fore.GREEN + "4. Port Scanner")
    print(Fore.GREEN + "5. GitHub User Scanner")
    print(Fore.RED + "0. Exit")


def main():
    banner()
    while True:
        menu()
        choice = input(Fore.YELLOW + "Select an option: ")
        if choice == '1':
            whois_lookup.run()
        elif choice == '2':
            dns_lookup.run()
        elif choice == '3':
            ip_tracker.run()
        elif choice == '4':
            port_scanner.run()
        elif choice == '5':
            github_user_scanner.run()
        elif choice == '0':
            print(Fore.CYAN + "Goodbye!")
            sys.exit()
        else:
            print(Fore.RED + "Invalid choice. Try again.")


if __name__ == "__main__":
    main()
