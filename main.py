import os
import getpass
import time
from colorama import Fore, Style
import ctypes

os.system('color')

webhook_link = None

ctypes.windll.kernel32.SetConsoleTitleA("made by doggydurgin or 006".encode('ascii'))

current_directory = f"C:\\Users\\{getpass.getuser()}\\AppData\\Local\\Discord"

directories = [d for d in os.listdir(current_directory) if os.path.isdir(os.path.join(current_directory, d))]
matching_directories = [d for d in directories if d.startswith("app-")]


for directory in matching_directories:
    directory_path = os.path.join(current_directory, directory)
    
    dir = f"{directory_path}\\modules\\discord_desktop_core-1\\discord_desktop_core\\index.js"
    
    with open(dir, "r+") as f:
        injectioncheck = f.read()
        if injectioncheck == "module.exports = require('./core.asar');" or injectioncheck == "module.exports = require('./core.asar');\n\n//hi from doggydurgin":
            print(f'{Style.BRIGHT}{Fore.GREEN}NO INJECTION LOG DETECTED')
            time.sleep(1.5)
        else:
            take_action = input(str(f"{Fore.RED}POSSIBLE INJECTION LOG DETECTED. TAKE ACTION? {Fore.YELLOW}(Y/N):{Fore.RESET} "))
            if "y" or "Y" in take_action:
                index = injectioncheck.find("https://discord.com/api/webhooks")
                if index != -1:
                    webhook_link = 'https://discord.com/api/webhooks/'
                    for char in injectioncheck[index + len('https://discord.com/api/webhooks/'):]:
                        if char.isalnum() or char in '/.-':
                            webhook_link += char
                        elif webhook_link.endswith(')'):
                            webhook_link = webhook_link[:-1]
                            continue
                        else:
                            continue
                f.seek(0)
                f.truncate()
                f.write("module.exports = require('./core.asar');\n\n//hi from doggydurgin")
                if webhook_link != None:
                    print(f"\n{Fore.GREEN}ACTION TAKEN. REVERSED INJECTION LOG: {Fore.YELLOW}{dir}")
                    print(f'{Fore.GREEN}WEBHOOK PULLED: {Fore.YELLOW}{webhook_link}')
                else:
                    print(f"\n{Fore.GREEN}ACTION TAKEN. REVERSED INJECTION LOG: {Fore.YELLOW}{dir}")
                    print(f'{Fore.RED}WEBHOOK NOT FOUND')

                time.sleep(1.5)
                input('YOU ARE NOW SAFE TO CHANGE YOUR PASSWORD ON DISCORD. PRESS ANY KEY TO EXIT')
            else:
                break
            
            
