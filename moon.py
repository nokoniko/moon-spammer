import time, requests, os, sys, base64
from pystyle import Colorate, Colors
from colorama import Fore

successful_commands = 0 

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

def get_webhook_name(webhook_url):
    response = requests.get(webhook_url)
    if response.status_code == 200:
        webhook_data = response.json()
        return webhook_data.get("name")
    else:
        return None

def update_webhook_name(webhook_url, new_name):
    global successful_commands
    payload = {"name": new_name}
    headers = {"Content-Type": "application/json"}
    response = requests.patch(webhook_url, json=payload, headers=headers)
    if response.status_code == 200:
        successful_commands += 1
        print(f"{Fore.GREEN}[!]{Fore.WHITE} Webhook name updated!")
    else:
        print(f"{Fore.RED}[!]{Fore.WHITE} Something went wrong: {response.status_code} - {response.text}")

def changepfp(webhook_url): # taken from https://github.com/infamouskoala/koalahook/blob/main/koalahook.py
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
        successful_commands += 1
        print(f"{Fore.GREEN}[!]{Fore.WHITE} Profile picture changed successfully.")
    except Exception as e:
        print(f"{Fore.RED}[!]{Fore.WHITE} Error: {e}")

def main(webhook_url, delay, amount, message):
    global successful_commands
    counter = 0
    try:
        while True if amount == "inf" else counter < int(amount):
            try:
                data = requests.post(webhook_url, json={"content": str(message)})
                if data.status_code == 204:
                    successful_commands += 1
                    print(f"{Fore.MAGENTA}[+]{Fore.WHITE} Sent '{message}' ({counter} times)")
                else:
                    print(f"{Fore.RED}[-]{Fore.WHITE} Failed to send message")
            except Exception as e:
                print(f"{Fore.RED}[!] Error: {e}")
            time.sleep(float(delay))
            counter += 1
    except KeyboardInterrupt:
        print(f"\n{Fore.GREEN}[!]{Fore.WHITE} Spam stopped by user. Total messages sent: {counter}")

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
        print(f" ║ {Fore.BLUE}[!]{Fore.WHITE} server-ID:  {guild_id} ║")
        time.sleep(0.1)
        print(f" ╚═════════════════════════════════════╝")
        time.sleep(0.1)
    else:
        print(f"    {Fore.RED}[!]{Fore.WHITE} something went wrong: {response.status_code} - {response.text}")
        
def gui():
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
    print(f" {Fore.BLUE}[i]{Fore.WHITE} Total successful commands: {successful_commands}")
    print()
    print(f" ┌──({name}㉿{Fore.MAGENTA}moon{Fore.WHITE})-[~]")
    print(f" └─{Fore.GREEN}${Fore.WHITE} Webhook info")
    get_webhook_details(webhook_url)
    print()
    time.sleep(1)
    animated_fast(" - - - - - - - - - - - - - - - -")
    print()
    print()
    gui()
    print(f" ┌──({name}㉿{Fore.MAGENTA}moon{Fore.WHITE})-[~]")
    valg2 = input(f" └─{Fore.GREEN}${Fore.WHITE} ").strip()
    print()
    print("")

    if valg2 == "-s":
        message = input(f"{Fore.BLUE}[?]{Fore.WHITE} Message to spam: ")
        delay = input(f"{Fore.BLUE}[?]{Fore.WHITE} Enter a delay [int/float] > ")
        amount = input(f"{Fore.BLUE}[?]{Fore.WHITE} Enter an amount [int/inf] > ")
        try:
            delay = float(delay)
        except ValueError:
            exit()
        else:
            main(webhook_url, delay, amount, message)
            time.sleep(1)
            os.system("cls" if os.name == "nt" else "clear")
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
        changepfp(webhook_url)
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
