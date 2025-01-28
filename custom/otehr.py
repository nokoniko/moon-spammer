import os, time

def set_window_title(title):
    if os.name == 'nt':
        import ctypes
        ctypes.windll.kernel32.SetConsoleTitleW(title)
    else:
        sys.stdout.write(f"\033]0;{title}\007")
        sys.stdout.flush()

def window_size(columns, rows):
    if os.name == 'nt':
        os.system(f"mode con: cols={columns} lines={rows}")
    else:
        sys.stdout.write(f"\033[8;{rows};{columns}t")
        sys.stdout.flush()

        
def print2():
    print()
    print()

def done():
    time.sleep(1)
    os.system("cls" if os.name == "nt" else "clear")