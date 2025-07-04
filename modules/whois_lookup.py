"""Whois Lookup Module"""

import whois
from colorama import Fore


def run():
    print(Fore.CYAN + "[Whois Lookup]")
    print("Enter a domain to fetch WHOIS information.")
    domain = input("Domain: ")
    try:
        data = whois.whois(domain)
        for key, value in data.items():
            print(f"{key}: {value}")
    except Exception:
        print(Fore.RED + "Invalid domain or network error.")
