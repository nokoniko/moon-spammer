import time, requests, os, sys, base64, threading
from pystyle import Colorate, Colors
from colorama import Fore
from custom.otehr import set_window_title, print2, done, window_size
from spammer.spammer import main
from custom.webhook_customise import *

window_size(120, 35)
set_window_title("MOON SPAMMER - BY NOKONIKO ON GITHUB")
os.system("cls" if os.name == "nt" else "clear")

gui  = """
                                    [!] -i. Webhook info
                                    [!] -s. Spam webhook
                                    [!] -d. Delete webhook
                                    [!] -r. Rename the webhook
                                    [!] -p. Change the webhook pfp          
                                    [!]  exit. Exits the program
                    
                    """



moon = r"""

                                  ___ ___     ___     ___     ___    
                                /' __` __`\  / __`\  / __`\ /' _ `\                 
                                /\ \/\ \/\ \/\ \L\ \/\ \L\ \/\ \/\ \ 
                                \ \_\ \_\ \_\ \____/\ \____/\ \_\ \_\
                                 \/_/\/_/\/_/\/___/  \/___/  \/_/\/_/   v 1.2
                     

"""
print(Colorate.Vertical(Colors.purple_to_blue, moon))
print("                                         ᴍᴀᴅᴇ ʙʏ ɴɪᴋᴏ <㇌")
print2()
print(f"{Fore.MAGENTA}[?]{Fore.WHITE} 1. Login with custom name")
print(f"{Fore.MAGENTA}[?]{Fore.WHITE} 2. Login as guest")
print()
valg = input(f"{Fore.MAGENTA}[?]{Fore.WHITE} Login meathod: ").strip()

if valg == "1":
    name = input(f"{Fore.MAGENTA}[?]{Fore.WHITE} What's your name: ")
elif valg == "2":
    name = "guest"
elif valg == "3": # fore testing
    exit()

webhook_url = input(f"{Fore.MAGENTA}[?]{Fore.WHITE} Webhook url: ").strip()
os.system("cls" if os.name == "nt" else "clear")
webhook_name = get_name(webhook_url)

while True:
    os.system("cls" if os.name == "nt" else "clear") 
    print(Colorate.Vertical(Colors.purple_to_blue, moon))
    print(f"                                Logged in as {Fore.MAGENTA}{name}{Fore.WHITE} with {Fore.MAGENTA}{webhook_name}{Fore.WHITE} as webhook")
    print2()
    print(Colorate.Vertical(Colors.purple_to_blue, gui))

    print(f" ┌──({name}㉿{Fore.MAGENTA}moon{Fore.WHITE})-[~]")
    valg2 = input(f" └─{Fore.GREEN}${Fore.WHITE} ").strip()
    print()
    if valg2 == "-i":
        webhook_info(webhook_url)
        time.sleep(4)
        os.system("cls" if os.name == "nt" else "clear")
    if valg2 == "-s":
        message = input(f"{Fore.MAGENTA}[?]{Fore.WHITE} Message to spam: ")
        delay = input(f"{Fore.MAGENTA}[?]{Fore.WHITE} Enter a delay [int/float] > ")
        amount = input(f"{Fore.MAGENTA}[?]{Fore.WHITE} Enter an amount [int/inf] > ")
        print()
        try:
            delay = float(delay)
        except ValueError:
            exit()
        else:
            # Starter `main` som en tråd
            spam_thread = threading.Thread(target=main, args=(webhook_url, delay, amount, message))
            spam_thread.start()
            print(f"{Fore.BLUE}[!] Spamming started in a background thread...")
            done()
    elif valg2 == "-d":
            delete_webhook(webhook_url)
            done()
    elif valg2 == "-r":
        new_name = input(f"{Fore.MAGENTA}[?]{Fore.WHITE} What you want the new name to be?: ").strip()
        update_name(webhook_url, new_name)
        webhook_name = get_name(webhook_url)
        done()
    elif valg2 == "-p":
        changepfp(webhook_url)
        done()
    elif valg2 == "exit":
        os.system("cls" if os.name == "nt" else "clear")
        print(f"bye bye {name}")
        break
    else:
        print(f"{Fore.RED}[!] Not a valid command.")
        done()