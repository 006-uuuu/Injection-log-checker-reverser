import os
import getpass
import time



current_directory = f"C:\\Users\\{getpass.getuser()}\\AppData\\Local\\Discord"

directories = [d for d in os.listdir(current_directory) if os.path.isdir(os.path.join(current_directory, d))]
matching_directories = [d for d in directories if d.startswith("app-")]


for directory in matching_directories:
    directory_path = os.path.join(current_directory, directory)
    
    dir = f"{directory_path}\\modules\\discord_desktop_core-1\\discord_desktop_core\\index.js"
    
    with open(dir, "r+") as f:
        injectioncheck = f.read()
        if injectioncheck == "module.exports = require('./core.asar');":
            print('NO INJECTION LOG DETECTED')
            time.sleep(1.5)
        else:
            take_action = input(str("POSSIBLE INJECTION LOG DETECTED. TAKE ACTION? (Y/N): "))
            if take_action == "y" and "Y":
                f.seek(0)
                f.truncate()
                f.write('''module.exports = require('./core.asar');''')
                print(f"\nACTION TAKEN. REVERSED INJECTION LOG: {dir}")
                time.sleep(1.5)
                print('YOU ARE NOW SAFE TO CHANGE YOUR PASSWORD ON DISCORD. STAY SAFE')
                time.sleep(5)
            else:
                break
            