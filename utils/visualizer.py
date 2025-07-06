import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_array(arr, highlight_indices=[], explanation=""):
    clear_screen()
    max_val = max(arr) if arr else 1
    print("\nArray Visualization:")
    for i, val in enumerate(arr):
        bar = "#" * int(val * 20 / max_val)  # Scale bars to fit console
        marker = "*" if i in highlight_indices else " "
        print(f"{i:2d} | {bar:<20} [{val}] {marker}")
    print(f"\nStep Explanation: {explanation}\n")

def display_search(arr, current_index, target, explanation=""):
    clear_screen()
    print(f"\nSearching for {target}:")
    for i, val in enumerate(arr):
        marker = "*" if i == current_index else " "
        print(f"{i:2d} | {val:3d} {marker}")
    print(f"\nStep Explanation: {explanation}\n")

def show_loading_animation():
    print("Processing", end="")
    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(0.3)
    print()