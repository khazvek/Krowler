"""DNS Lookup Module"""

import dns.resolver
from colorama import Fore


def run():
    print(Fore.CYAN + "[DNS Lookup]")
    print("Enter a domain to resolve DNS records (A records).")
    domain = input("Domain: ")
    try:
        answers = dns.resolver.resolve(domain, 'A')
        for rdata in answers:
            print(f"A Record: {rdata.address}")
    except Exception as e:
        print(Fore.RED + f"Error: {e}")
