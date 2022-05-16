import time
import datetime as date
import os
import shutil as s

# Log File creation with creation info
log_file_path = input("Insert the log file path ")
log_file_path = log_file_path + '\log_file.txt'
with open(f'{log_file_path}', 'w') as log:
    log.write(f"{date.datetime.now().strftime('%m/%d/%Y,%H:%M:%S')}, Log File Creation at: {log_file_path}")
    print(f"{date.datetime.now().strftime('%m/%d/%Y,%H:%M:%S')} Created Log file at: {log_file_path}")

# Creation Source Folder if it doesn't exist
source_folder_path = input("Insert the Source folder path ")
source_folder_path = source_folder_path + '\Source'
try:
    os.mkdir(f'{source_folder_path}')
    with open(f'{log_file_path}', 'a') as log:
        log.write(
            f"\n{date.datetime.now().strftime('%m/%d/%Y,%H:%M:%S')}, Created Source folder at: {source_folder_path}")
    print(f"{date.datetime.now().strftime('%m/%d/%Y,%H:%M:%S')} Created Source folder at: {source_folder_path}")
except:
    print("Source Folder already exist")

# Creation Replica Folder if doesn't exist
replica_folder_path = input("Insert the Replica folder path ")
replica_folder_path = replica_folder_path + '\Replica'
try:
    os.mkdir(f'{replica_folder_path}')
    with open(f'{log_file_path}', 'a') as log:
        log.write(
            f"\n{date.datetime.now().strftime('%m/%d/%Y,%H:%M:%S')}, Created Replica folder at: {replica_folder_path}")
    print(f"{date.datetime.now().strftime('%m/%d/%Y,%H:%M:%S')} Created Replica folder at: {replica_folder_path}")
except:
    print("Replica Folder already exist")

# Time Interval calculation based on user input
while True:
    interval_type = input("The amount of time should be calculate in seconds, minutes or days ").lower()

    if interval_type == "days":
        time_interval = int(input(f"Insert the amount of {interval_type} "))
        sincro_delay = (time_interval * 86400)
        break

    elif interval_type == "minutes":
        time_interval = int(input(f"Insert the amount of {interval_type} "))
        sincro_delay = (time_interval * 60)
        break

    elif interval_type == "seconds":
        time_interval = int(input(f"Insert the amount of {interval_type} "))
        sincro_delay = time_interval
        break
    else:
        print("the please insert a valid time unit")

with open(f'{log_file_path}', 'a') as log:
    log.write(
        f"\n{date.datetime.now().strftime('%m/%d/%Y,%H:%M:%S')}, Synchronization Started")
print(f"{date.datetime.now().strftime('%m/%d/%Y,%H:%M:%S')} Synchronization Started")

# Synchronization created
while True:
    # Copy Files from Source folder to Replica folder
    for file in os.listdir(source_folder_path):
        if file in os.listdir(replica_folder_path):
            s.copy2(f"{source_folder_path}\{file}", f"{replica_folder_path}")
        else:
            s.copy2(f"{source_folder_path}\{file}", f"{replica_folder_path}")
            with open(f'{log_file_path}', 'a') as log:
                log.write(f"\n{date.datetime.now().strftime('%m/%d/%Y,%H:%M:%S')}, Copied file: {file}")
            print(f"{date.datetime.now().strftime('%m/%d/%Y,%H:%M:%S')} Copied file: {file}")

    # Remove Files from Replica folder if not in Source Folder
    for file in os.listdir(f"{replica_folder_path}"):
        if file not in os.listdir(f"{source_folder_path}"):
            file_path = f'{replica_folder_path}\{file}'
            os.remove(file_path)
            with open(f'{log_file_path}', 'a') as log:
                log.write(f"\n{date.datetime.now().strftime('%m/%d/%Y,%H:%M:%S')}, Removed file: {file}")
            print(f"{date.datetime.now().strftime('%m/%d/%Y,%H:%M:%S')} Removed file: {file}")



    time.sleep(sincro_delay)
