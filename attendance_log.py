import os
from datetime import datetime

def attendance_log(name,timestamp):
    new_entry = f"{name} attended the meeting at {timestamp}\n"
    if os.path.exists("example.txt"):
        with open("example.txt", "r+") as f:
            content = f.read()
            f.seek(0, 0)
            f.write( new_entry+ content)
    else:
        with open("example.txt", "w") as f:
            f.write(new_entry)
while True:
    name=input("Enter your name (or 'exit' to quit): ")
    timestamp = datetime.now().strftime("%d-%b-%Y %H:%M:%S")

    if name.lower()=="exit":
        if os.path.exists("example.txt"):
            with open("example.txt", "r+") as f:
                content = f.read()
                f.seek(0, 0)
                f.write(f"Exiting attendance logger at {timestamp}\n"+content)
        print(f"Attendance logger ended at {timestamp}")
        break
    else:
        attendance_log(name,timestamp)
        print(f"👋 Welcome {name}! Attendance recorded. Wishing you a wonderful day!")
