import time, requests, os, sys
from pystyle import Colorate, Colors
from colorama import Fore


def set_window_title(title):
    if os.name == 'nt':
        import ctypes
        ctypes.windll.kernel32.SetConsoleTitleW(title)
    else:
        sys.stdout.write(f"\033]0;{title}\007")
        sys.stdout.flush()

def set_window_size(columns, rows):
    if os.name == 'nt':
        os.system(f"mode con: cols={columns} lines={rows}")
    else:
        sys.stdout.write(f"\033[8;{rows};{columns}t")
        sys.stdout.flush()


set_window_size(90, 40)
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
        
        print(f" ╔═════════════════════════════════════╗")
        time.sleep(0.1)
        print(f" ║ {Fore.BLUE}[!]{Fore.WHITE} hook: {webhook_name:<19}       ║")
        time.sleep(0.1)
        print(f" ║ {Fore.BLUE}[!]{Fore.WHITE} channel-ID: {channel_id} ║")
        time.sleep(0.1)
        print(f" ║ {Fore.BLUE}[!]{Fore.WHITE} channel-ID: {channel_id} ║")
        time.sleep(0.1)
        print(f" ║ {Fore.BLUE}[!]{Fore.WHITE} server-ID: {guild_id}  ║")
        time.sleep(0.1)
        print(f" ╚═════════════════════════════════════╝")
        time.sleep(0.1)
    else:
        print(f"    {Fore.RED}[!]{Fore.WHITE} something went wrong: {response.status_code} - {response.text}")

def spam_webhook(webhook_url, message):
    counter = 0
    try:
        while True:
            response = requests.post(webhook_url, json={"content": message})
            if response.status_code == 204:
                counter += 1
                print(f"{Fore.MAGENTA}[+]{Fore.WHITE} Sent '{message}' ({counter} times)")
            elif response.status_code == 429:  # Rate limit
                retry_after = response.json().get("retry_after", 3) / 3000  # Millisekunder til sekunder
                print(f"{Fore.RED}[!] Rate limited. Waiting {retry_after:.2f} seconds.")
                time.sleep(retry_after)
            else:
                print(f"{Fore.RED}[!] Error: {response.status_code} - {response.text}")
                break
    except KeyboardInterrupt:
        print(f"\n{Fore.GREEN}[!]{Fore.WHITE} Spam stopped by user. Total messages sent: {counter}")

    

def animated_print(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

def animated_fast(text, delay=0.01):
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
                     \/_/\/_/\/_/\/___/  \/___/  \/_/\/_/    v 1.1
                     

"""
print(Colorate.Vertical(Colors.purple_to_blue, moon))
animated_print("                          ᴍᴀᴅᴇ ʙʏ ɴɪᴋᴏ <㇌")
print()
print()
print(f"{Fore.BLUE}[?]{Fore.WHITE} 1. Login with custom name")
print(f"{Fore.BLUE}[?]{Fore.WHITE} 2. Login as guest")
print()
valg = input(f"{Fore.BLUE}[?]{Fore.WHITE} Login meathod: ").strip()

if valg == "1":
    name = input(f"{Fore.BLUE}[?]{Fore.WHITE} What's your name: ")
elif valg == "2":
    name = "guest"

webhook_url = input(f"{Fore.BLUE}[?]{Fore.WHITE} Webhook url: ").strip()
os.system("cls" if os.name == "nt" else "clear")
webhook_name = get_webhook_name(webhook_url)

while True:
    os.system("cls" if os.name == "nt" else "clear")
    print(Colorate.Vertical(Colors.purple_to_blue, moon))  # Logo
    animated_print("                           made by niko")
    print(f"{Fore.WHITE}")
    print(f"                Logged in as {Fore.BLUE}{name}{Fore.WHITE} with {Fore.BLUE}{webhook_name}{Fore.WHITE} as webhook")
    print(f"{Fore.WHITE}")
    print()
    print(f" ┌──({name}㉿{Fore.MAGENTA}moon{Fore.WHITE})-[~]")
    print(f" └─{Fore.GREEN}${Fore.WHITE} Webhook info")
    get_webhook_details(webhook_url)
    print()
    time.sleep(1)
    animated_fast(" - - - - - - - - - - - - - - - -")
    print()
    print()
    print(f" ┌──({name}㉿{Fore.MAGENTA}moon{Fore.WHITE})-[~]")
    print(f" └─{Fore.GREEN}${Fore.WHITE} Webhook commands")
    print(f" ╔══════════════════════════════════╗")
    time.sleep(0.1)
    print(f" ║ {Fore.BLUE}[!]{Fore.WHITE} -s. Spam webhook             ║")
    time.sleep(0.1)
    print(f" ║ {Fore.BLUE}[!]{Fore.WHITE} -d. Delete webhook           ║")
    time.sleep(0.1)
    print(f" ║ {Fore.BLUE}[!]{Fore.WHITE} -r. Rename the webhook       ║")
    time.sleep(0.1)
    print(f" ║ {Fore.BLUE}[!]{Fore.WHITE} -p. Changes the webhook pfp  ║")
    time.sleep(0.1)
    print(f" ║ {Fore.BLUE}[!]{Fore.WHITE} exit. Exits the program      ║")
    time.sleep(0.1)
    print(f" ╚══════════════════════════════════╝")
    time.sleep(0.1)
    print()
    print(f" ┌──({name}㉿{Fore.MAGENTA}moon{Fore.WHITE})-[~]")
    valg2 = input(f" └─{Fore.GREEN}${Fore.WHITE} ").strip()
    print()
    print("")

    if valg2 == "-s":
        message = input(f"{Fore.BLUE}[?]{Fore.WHITE} Message to spam: ").strip()
        spam_webhook(webhook_url, message)
    elif valg2 == "-d":
        response = requests.delete(webhook_url)
        if response.status_code == 204:
            print(Colorate.Vertical(Colors.blue_to_purple, "[!] Webhooken deleted!"))
            time.sleep(1)
            os.system("cls" if os.name == "nt" else "clear")
        else:
            print(f"{Fore.RED}[!]{Fore.WHITE} Something went wrong: {response.status_code} - {response.text} [!]")
            time.sleep(1)
            os.system("cls" if os.name == "nt" else "clear")
    elif valg2 == "-r":
        new_name = input(f"{Fore.BLUE}[?]{Fore.WHITE} What you want the new name to be?: ").strip()
        update_webhook_name(webhook_url, new_name)
        webhook_name = get_webhook_name(webhook_url)
        time.sleep(1)
        os.system("cls" if os.name == "nt" else "clear")
    elif valg2 == "-p":
        new_avatar_url = input(f"{Fore.BLUE}[?]{Fore.WHITE} URL to webhook pfp: ").strip()
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
