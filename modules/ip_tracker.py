"""IP Tracker Module"""

import requests
from colorama import Fore

API_URL = "http://ip-api.com/json/"  # No API key needed


def run():
    print(Fore.CYAN + "[IP Tracker]")
    print("Enter an IP address to geolocate.")
    ip = input("IP Address: ")
    try:
        response = requests.get(API_URL + ip, timeout=10)
        data = response.json()
        if data.get("status") == "success":
            for key in ["query", "country", "regionName", "city", "isp", "org", "lat", "lon"]:
                print(f"{key}: {data.get(key)}")
        else:
            print(Fore.RED + "Lookup failed")
    except Exception as e:
        print(Fore.RED + f"Error: {e}")
