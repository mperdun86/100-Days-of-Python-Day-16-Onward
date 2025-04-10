#THIS IS A QUICK SCRIPT I MADE TO POPULATE THE PROJECT WITH FOLDERS
import os

for i in range(30, 101):  # From Day 30 to Day 100
    day_folder = f"Day {i}"
    notes_folder = os.path.join(day_folder, "notes")
    
    os.makedirs(notes_folder, exist_ok=True)