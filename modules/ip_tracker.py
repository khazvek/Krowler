"""IP Tracker Module"""

import requests
from colorama import Fore

# ip-api.com only offers HTTPS on paid plans. The free tier is HTTP only,
# which is why this endpoint uses HTTP.
API_URL = "http://ip-api.com/json/"  # No API key needed


def run():
    print(Fore.CYAN + "[IP Tracker]")
    print("Enter an IP address to geolocate.")
    ip = input("IP Address: ")
    try:
        response = requests.get(API_URL + ip, timeout=10)
        response.raise_for_status()
        data = response.json()
        if data.get("status") == "success":
            for key in [
                "query",
                "country",
                "regionName",
                "city",
                "isp",
                "org",
                "lat",
                "lon",
            ]:
                print(f"{key}: {data.get(key)}")
        else:
            print(Fore.RED + data.get("message", "Lookup failed"))
    except requests.exceptions.Timeout:
        print(Fore.RED + "Request timed out.")
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"Request error: {e}")
    except Exception as e:
        print(Fore.RED + f"Error: {e}")
