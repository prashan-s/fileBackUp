import os
import shutil
import subprocess
import time
from datetime import datetime

#source = r"C:\TS\HWS"
#dest = r"E:\Educational\HWS"
source = r"C:\TS\HWS"
dest = r"E:\Educational\HWS"
threshold = 1024  # in megabytes
interval = 5 * 60  # in seconds
fastcopy = "fastcopy.exe"

# Get the current date and time
dateTimeFormat = "%Y-%m-%d_%H-%M-%S"

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print("Next Backup cycle in ",timer,".", end='\r')
        time.sleep(1)
        t -= 1

    print('\nTime\'s up!')
    
while True:
    now = datetime.now()
    current_time = now.strftime(dateTimeFormat)
    print("---------------------------------------------------------------------------")
    print("● CurrentTime: ",current_time)
    print("● Checking the size of the source directory...")
    size = sum(sum(os.path.getsize(os.path.join(dirpath, filename)) for filename in filenames) for dirpath, _, filenames in os.walk(source)) // 1024 // 1024
    print(f"\n● The size of the source directory is {size} MB.")
    if size > threshold:
        print(f"\n● The source directory has exceeded the threshold size of {threshold} MB.\nLogging the names of the source directory files...")
        
        # Get the current date and time
        now = datetime.now()
        current_time = now.strftime(dateTimeFormat)
        
        # Log the names of the source directory files to the operations file
        with open("operations.txt", "a") as f:
            f.write(f"-Source directory files as of {current_time}:\n")
            for root, dirs, files in os.walk(source):
                for file in files:
                    f.write(f"{os.path.join(root, file)}\n")
            
            print(f"\n● Moving the directory to the destination using {fastcopy}...")
            subprocess.run([fastcopy, "/cmd=move ","/force_close ", "/to=" + dest, source])
            
            # Get the current date and time
            now = datetime.now()
            current_time = now.strftime(dateTimeFormat)
            f.write(f"-Operation completed at {current_time}:\n\n")
        print("\n● The directory has been moved to the destination.")
        print("---------------------------------------------------------------------------\n\n")
        time.sleep(1)
    else:
        print(f"● The size of the source directory is below the threshold size of {threshold} MB.\n\n● Waiting for {interval} seconds...")
        
        countdown(interval)


