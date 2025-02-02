import requests, time
from colorama import Fore


def main(webhook_url, delay, amount, message):
    global successful_commands
    counter = 0
    try:
        while True if amount == "inf" else counter < int(amount):
            try:
                data = requests.post(webhook_url, json={"content": str(message)})
                if data.status_code == 204:
                    successful_commands += 1
                    print(f"{Fore.MAGENTA}[+]{Fore.WHITE} Sent {message} {counter + 1} times")
                else:
                    print(f"{Fore.RED}[-]{Fore.WHITE} Failed to send message")
            except Exception as e:
                print(f"{Fore.RED}[!] Error: {e}")
            time.sleep(float(delay))
            counter += 1
        print(f"{Fore.GREEN}[!] Done.")
    except KeyboardInterrupt:
        print(f"\n{Fore.GREEN}[!]{Fore.WHITE} Spam stopped by user. Total messages sent: {counter}")
