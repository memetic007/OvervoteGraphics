import csv
from pynput import keyboard
import platform
import os

def read_data_from_csv(filename):
    """
    Reads a CSV file and converts it into a list of tuples.
    Each tuple contains a string and a float of any size.

    Parameters:
    - filename: The name of the CSV file to read.

    Returns:
    - A list of tuples (string, float).
    """
    data = []
    with open(filename, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for idx, row in enumerate(reader):
            if len(row) >= 2:
                label = row[0].strip()
                try:
                    value = float(row[1])
                    data.append((label, value))
                except ValueError:
                    print(f"Warning: Invalid numeric value '{row[1]}' at line {idx + 1}. Skipping this entry.")
            else:
                print(f"Warning: Not enough columns at line {idx + 1}. Skipping this entry.")
    return data

def wait_for_spacebar():
    print("Press the space bar to continue...")
    
    space_pressed = False
    
    def on_press(key):
        nonlocal space_pressed
        if key == keyboard.Key.space:
            space_pressed = True
            return False  # Stop listener
    
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
    
    print("Space bar pressed. Continuing...")

def wait_for_enter():
    print("Press Enter to continue...", end='', flush=True)
    while True:
        key = input().strip()
        if key == "":
            break
    print("Enter pressed. Continuing...")

def clear_terminal():
    # Check the operating system
    if platform.system() == "Windows":
        os.system("cls")  # Clear command for Windows
    else:
        os.system("clear")  # Clear command for Unix/Linux/Mac