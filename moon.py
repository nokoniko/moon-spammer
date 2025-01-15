import time, requests, os, sys
from pystyle import Colorate, Colors
from colorama import Fore
from dhooks import Webhook


def set_window_title(title):
    if os.name == 'nt':
        import ctypes
        ctypes.windll.kernel32.SetConsoleTitleW(title)
    else:
        sys.stdout.write(f"\033]0;{title}\007")
        sys.stdout.flush()

def set_terminal_size(columns, lines):
    os.system(f"printf '\e[8;{lines};{columns}t'")

set_terminal_size(130, 50)
set_window_title("MOON SPAMMER - BY NOKONIKO ON GITHUB")

os.system("cls" if os.name == "nt" else "clear")

def get_webhook_name(webhook_url):
    response = requests.get(webhook_url)
    if response.status_code == 200:
        webhook_data = response.json()
        return webhook_data.get("name")
    else:
        return None

def update_webhook_name(webhook_url, new_name):
    payload = {"name": new_name}
    headers = {"Content-Type": "application/json"}
    response = requests.patch(webhook_url, json=payload, headers=headers)

    if response.status_code == 200:
        print(f"{Fore.GREEN}[!]{Fore.WHITE} webhook name updated!")
    else:
        print(f"{Fore.RED}[!]{Fore.WHITE} something went wrog: {response.status_code} - {response.text}")

def update_webhook_profile(webhook_url, new_avatar_url):
    payload = {
        "avatar": new_avatar_url 
    }
    headers = {
        "Content-Type": "application/json"
    }
    
    response = requests.patch(webhook_url, json=payload, headers=headers)
    
    if response.status_code == 200:
        print(f"{Fore.GREEN}[!]{Fore.WHITE} webhook pfp updated!")
    else:
        print(f"{Fore.RED}[!]{Fore.WHITE} something went wrong: {response.status_code} - {response.text}")

def get_webhook_details(webhook_url):
    response = requests.get(webhook_url)
    if response.status_code == 200:
        webhook_data = response.json()
        channel_id = webhook_data.get("channel_id")
        guild_id = webhook_data.get("guild_id")
        webhook_name = webhook_data.get("name")
        
        print(f"{Fore.BLUE}[!]{Fore.WHITE} Webhook-name: {webhook_name}")
        print(f"{Fore.BLUE}[!]{Fore.WHITE} channel-ID: {channel_id}")
        print(f"{Fore.BLUE}[!]{Fore.WHITE} server-ID: {guild_id}")
    else:
        print(f"{Fore.RED}[!]{Fore.WHITE} something went wrong: {response.status_code} - {response.text}")

def animated_print(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

set_window_title("MOON SPAMMER - BY NOKONIKO ON GITHUB")

moon = r"""

                  ___ ___     ___     ___     ___    
                /' __` __`\  / __`\  / __`\ /' _ `\  
                /\ \/\ \/\ \/\ \L\ \/\ \L\ \/\ \/\ \ 
                \ \_\ \_\ \_\ \____/\ \____/\ \_\ \_\
                 \/_/\/_/\/_/\/___/  \/___/  \/_/\/_/    v 1.0

"""
print(Colorate.Vertical(Colors.purple_to_blue, moon))
animated_print("                          ᴍᴀᴅᴇ ʙʏ ɴɪᴋᴏ <㇌")
print()
print()
print(f"{Fore.BLUE}[?]{Fore.WHITE} 1. login with custom name")
print(f"{Fore.BLUE}[?]{Fore.WHITE} 2. login as guest")
print()
valg = input(f"{Fore.BLUE}[?]{Fore.WHITE} login meathod: ").strip()

if valg == "1":
    name = input(f"{Fore.BLUE}[?]{Fore.WHITE} what's your name: ")
elif valg == "2":
    name = "guest"

webhook_url = input(f"{Fore.BLUE}[?]{Fore.WHITE} webhook url: ").strip()
os.system("cls" if os.name == "nt" else "clear")
webhook_name = get_webhook_name(webhook_url)

while True:
    os.system("cls" if os.name == "nt" else "clear")
    print(Colorate.Vertical(Colors.purple_to_blue, moon))  # Logo
    animated_print("                           made by niko")
    print(f"{Fore.WHITE}")
    print(f"                logged in as {Fore.BLUE}{name}{Fore.WHITE} with {Fore.BLUE}{webhook_name}{Fore.WHITE} as webhook")
    print(f"{Fore.WHITE}")
    print()
    print("webhook info")
    get_webhook_details(webhook_url)
    print()
    print(" - - - - - - - - - - - - - - - -")
    print()
    print("webhook commands")
    print(f"{Fore.BLUE}[!]{Fore.WHITE} -s. spam webhook")
    print(f"{Fore.BLUE}[!]{Fore.WHITE} -d. delete webhook")
    print(f"{Fore.BLUE}[!]{Fore.WHITE} -r. rename the webhook")
    print(f"{Fore.BLUE}[!]{Fore.WHITE} -p. changes the webhook pfp")
    print(f"{Fore.BLUE}[!]{Fore.WHITE} exit. exits the program")
    print()
    print(f"┌──({name}㉿{Fore.MAGENTA}moon{Fore.WHITE})-[~]")
    valg2 = input("└─$ ").strip()
    print()
    print("")

    if valg2 == "-s":
        message = input(f"{Fore.BLUE}[?]{Fore.WHITE} What do you want to spam?: ")
        delay = int(input(f"{Fore.BLUE}[?]{Fore.WHITE} Enter a delay: "))

        counter = 0
        print(Colorate.Vertical(Colors.blue_to_purple, "[!] Spamming... Press Ctrl+C to stop."))
        try:
            while True:
                time.sleep(delay)
                Webhook(webhook_url).send(message)
                counter += 1
                print(f"{Fore.MAGENTA}[+]{Fore.WHITE} Sent '{message}' ({counter} times)")
        except KeyboardInterrupt:
            print(Colorate.Vertical(Colors.blue_to_purple, "[!] Spamming stopped."))
            time.sleep(1)
            os.system("cls" if os.name == "nt" else "clear")
    elif valg2 == "-d":
        response = requests.delete(webhook_url)
        if response.status_code == 204:
            print(Colorate.Vertical(Colors.blue_to_purple, "[!] Webhooken deleted!"))
            time.sleep(1)
            os.system("cls" if os.name == "nt" else "clear")
        else:
            print(f"{Fore.RED}[!]{Fore.WHITE} something went wrong: {response.status_code} - {response.text} [!]")
            time.sleep(1)
            os.system("cls" if os.name == "nt" else "clear")
    elif valg2 == "-r":
        new_name = input(f"{Fore.BLUE}[?]{Fore.WHITE} what you want the new name to be?: ").strip()
        update_webhook_name(webhook_url, new_name)
        webhook_name = get_webhook_name(webhook_url)
        time.sleep(1)
        os.system("cls" if os.name == "nt" else "clear")
    elif valg2 == "-p":
        new_avatar_url = input(f"{Fore.BLUE}[?]{Fore.WHITE} url to webhook pfp: ").strip()
        update_webhook_profile(webhook_url, new_avatar_url)
        time.sleep(1)
        os.system("cls" if os.name == "nt" else "clear")
    elif valg2 == "exit":
        os.system("cls" if os.name == "nt" else "clear")
        animated_print(f"bye bye {name}")
        time.sleep(1)
        break
    else:
        print(Colorate.Vertical(Colors.red, "[!] Not a valid command."))
        time.sleep(1)
        os.system("cls" if os.name == "nt" else "clear")
