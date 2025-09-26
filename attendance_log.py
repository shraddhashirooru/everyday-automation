import os
from datetime import datetime

def attendance_log(name,timestamp):
    """Logs attendance of a person with a timestamp.

    Steps:
    1. Check if the attendance file ("example.txt") exists.
    2. If it exists:
        - Read its current content.
        - Prepend the new attendance entry at the top.
    3. If it does not exist:
        - Create a new file and write the attendance entry.
    4. Format of each entry: "[Name] attended the meeting at [Timestamp]"

    Args:
        name (str): Name of the person attending.
        timestamp (str): The timestamp of attendance in string format."""
    new_entry = f"{name} attended the meeting at {timestamp}\n"
    if os.path.exists("example.txt"):
        # File exists, read current content and prepend new entry

        with open("example.txt", "r+") as f:
            content = f.read()
            f.seek(0, 0) # Go to the beginning of the file
            f.write(new_entry+ content)
    else:
        # File does not exist, create and write entry
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
        break #stop the program if input is 'exit'
    else:
        attendance_log(name,timestamp)
        # Display welcome message for each person who enters their name
        print(f"👋 Welcome {name}! Attendance recorded. Wishing you a wonderful day!")
