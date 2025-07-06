import os
import time

def get_user_array():
    while True:
        try:
            arr = input("Enter numbers separated by spaces (e.g., 5 2 8 1): ").strip().split()
            arr = [int(x) for x in arr]
            if len(arr) < 2:
                print("Please enter at least 2 numbers.")
                continue
            return arr
        except ValueError:
            print("Invalid input! Enter integers separated by spaces.")

def validate_speed():
    while True:
        try:
            speed = float(input("Enter visualization speed (seconds per step, e.g., 0.5): "))
            if speed < 0:
                print("Speed must be non-negative.")
                continue
            return speed
        except ValueError:
            print("Invalid input! Enter a number (e.g., 0.5).")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')