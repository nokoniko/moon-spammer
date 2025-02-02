import time, requests, os, sys, base64, threading
from pystyle import Colorate, Colors
from colorama import Fore

def get_name(webhook_url):
    response = requests.get(webhook_url)
    if response.status_code == 200:
        webhook_data = response.json()
        return webhook_data.get("name")
    else:
        return None
    
def delete_webhook(webhook_url):
    response = requests.delete(webhook_url)
    if response.status_code == 204:
        print(Colorate.Vertical(Colors.blue_to_purple, " [!] Webhooken deleted!"))
        time.sleep(1)
        os.system("cls" if os.name == "nt" else "clear")
    else:
        print(f"{Fore.RED}[!]{Fore.WHITE} Something went wrong: {response.status_code} - {response.text} [!]")
        
def update_name(webhook_url, new_name):
    global successful_commands
    payload = {"name": new_name}
    headers = {"Content-Type": "application/json"}
    response = requests.patch(webhook_url, json=payload, headers=headers)
    if response.status_code == 200:
        print(f"{Fore.GREEN}[!]{Fore.WHITE} Webhook name updated!")
    else:
        print(f"{Fore.RED}[!]{Fore.WHITE} Something went wrong: {response.status_code} - {response.text}")

def changepfp(webhook_url):
    global successful_commands
    image_path = input(f"{Fore.BLUE}[?]{Fore.WHITE} Path/URL to image: ").strip()
    try:
        if image_path.startswith(('http://', 'https://')):
            response = requests.get(image_path)
            response.raise_for_status()
            encoded_image = base64.b64encode(response.content).decode('utf-8')
        else:
            with open(image_path, "rb") as image_file:
                encoded_image = base64.b64encode(image_file.read()).decode('utf-8')

        data = {
            "avatar": f"data:image/jpeg;base64,{encoded_image}"
        }
        response = requests.patch(webhook_url, json=data)
        response.raise_for_status()
        print(f"{Fore.GREEN}[!]{Fore.WHITE} Profile picture changed successfully.")
    except Exception as e:
        print(f"{Fore.RED}[!]{Fore.WHITE} Error: {e}")
        
def webhook_info(webhook_url):
    response = requests.get(webhook_url)
    if response.status_code == 200:
        webhook_data = response.json()
        channel_id = webhook_data.get("channel_id")
        guild_id = webhook_data.get("guild_id")
        webhook_name = webhook_data.get("name")
        
        print(f" {Fore.MAGENTA}[!]{Fore.WHITE} hook: {webhook_name}")
        print(f" {Fore.MAGENTA}[!]{Fore.WHITE} channel-ID: {channel_id}")
        print(f" {Fore.MAGENTA}[!]{Fore.WHITE} channel-ID: {channel_id}")
        print(f" {Fore.MAGENTA}[!]{Fore.WHITE} server-ID:  {guild_id}")
