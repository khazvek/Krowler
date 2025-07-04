"""GitHub User Scanner Module"""

import requests
from colorama import Fore

API_URL = "https://api.github.com/users/"


def run():
    print(Fore.CYAN + "[GitHub User Scanner]")
    print("Enter a GitHub username to fetch public profile data.")
    username = input("Username: ")
    try:
        response = requests.get(API_URL + username, timeout=10)
        if response.status_code == 404:
            print(Fore.RED + "User not found.")
            return
        response.raise_for_status()
        data = response.json()
        for key in [
            "login",
            "public_repos",
            "followers",
            "following",
            "html_url",
        ]:
            print(f"{key}: {data.get(key)}")
    except requests.exceptions.Timeout:
        print(Fore.RED + "Request timed out.")
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"Request error: {e}")
    except Exception as e:
        print(Fore.RED + f"Error: {e}")
