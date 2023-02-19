import os
import shutil
import subprocess
import time
from datetime import datetime

#source = r"C:\TS\HWS"
#dest = r"E:\Educational\HWS"
source = r"C:\Test\T"
dest = r"E:\Hello\NewT"
threshold = 100  # in megabytes
interval = 1  # in seconds
fastcopy = "fastcopy.exe"

# Get the current date and time
now = datetime.now()
current_time = now.strftime("%Y-%m-%d_%H-%M-%S")

while True:
    print("\n\n-----------------------------------------------------------")
    print("CurrentTime: ",current_time)
    print("\nChecking the size of the source directory...")
    size = sum(sum(os.path.getsize(os.path.join(dirpath, filename)) for filename in filenames) for dirpath, _, filenames in os.walk(source)) // 1024 // 1024
    print(f"\nThe size of the source directory is {size} MB.")
    if size > threshold:
        print(f"\nThe source directory has exceeded the threshold size of {threshold} MB. Logging the names of the source directory files...")
        
        # Get the current date and time
        now = datetime.now()
        current_time = now.strftime("%Y-%m-%d_%H-%M-%S")
        
        # Log the names of the source directory files to the operations file
        with open("operations.txt", "a") as f:
            f.write(f"Source directory files as of {current_time}:\n")
            for root, dirs, files in os.walk(source):
                for file in files:
                    f.write(f"{os.path.join(root, file)}\n")
        
        print(f"\nMoving the directory to the destination using {fastcopy}...")
        subprocess.run([fastcopy, "/cmd=move ","/force_close ", "/to=" + dest, source])
        print("\nThe directory has been moved to the destination.")
        print("-----------------------------------------------------------")
        time.sleep(1)
    else:
        print(f"The size of the source directory is below the threshold size of {threshold} MB. Waiting for {interval} seconds...")
        time.sleep(interval)
