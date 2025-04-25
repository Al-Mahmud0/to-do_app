import random
import time
import os
from colorama import Fore, Style, init
import shutil

# Init colorama
init(autoreset=True)

# Characters pool
chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+-=[]{}|;:',.<>?/"

# Colors for effect
colors = [Fore.GREEN, Fore.RED, Fore.YELLOW, Fore.BLUE, Fore.CYAN, Fore.MAGENTA]

def get_terminal_size():
    size = shutil.get_terminal_size()
    return size.columns, size.lines

def generate_line(width):
    return ''.join(random.choice(chars) for _ in range(width))

def hacking_screen():
    try:
        while True:
            width, height = get_terminal_size()
            os.system('cls' if os.name == 'nt' else 'clear')

            for _ in range(height):
                color = random.choice(colors)
                line = generate_line(width)
                print(color + line)

            time.sleep(0.1)  # Control refresh rate
    except KeyboardInterrupt:
        print(Fore.RED + "\nSimulation exited. Have a nice day!")

# Run the full screen simulator
hacking_screen()
