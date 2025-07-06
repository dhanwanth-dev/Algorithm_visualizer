import time
from algorithms.sorting import bubble_sort, selection_sort, insertion_sort, merge_sort, quick_sort, heap_sort
from algorithms.searching import linear_search, binary_search
from utils.visualizer import display_array, display_search, show_loading_animation
from utils.helpers import get_user_array, validate_speed, clear_screen

def main_menu():
    print("\n=== Console Algorithm Visualizer ===")
    print("1. Sorting Algorithms")
    print("2. Searching Algorithms")
    print("3. Exit")
    choice = input("Enter your choice (1-3): ")
    return choice

def sorting_menu():
    print("\n=== Sorting Algorithms ===")
    print("1. Bubble Sort")
    print("2. Selection Sort")
    print("3. Insertion Sort")
    print("4. Merge Sort")
    print("5. Quick Sort")
    print("6. Heap Sort")
    choice = input("Enter your choice (1-6): ")
    return choice

def searching_menu():
    print("\n=== Searching Algorithms ===")
    print("1. Linear Search")
    print("2. Binary Search (requires sorted array)")
    choice = input("Enter your choice (1-2): ")
    return choice

def run_sorting_algorithm(choice, arr):
    sort_functions = {
        '1': bubble_sort,
        '2': selection_sort,
        '3': insertion_sort,
        '4': merge_sort,
        '5': quick_sort,
        '6': heap_sort
    }
    if choice in sort_functions:
        show_loading_animation()
        arr_copy = arr.copy()
        steps, stats = sort_functions[choice](arr_copy)
        navigate_steps(steps, "sorting")
        print(f"\nFinal Sorted Array: {arr_copy}")
        print(f"Comparisons: {stats['comparisons']}, Swaps: {stats['swaps']}")
        print(f"Time Complexity: {stats['time_complexity']}")
    else:
        print("Invalid choice!")

def run_searching_algorithm(choice, arr, target, speed):
    search_functions = {
        '1': linear_search,
        '2': binary_search
    }
    if choice == '2' and arr != sorted(arr):
        print("Binary Search requires a sorted array. Sorting first...")
        show_loading_animation()
        arr.sort()
    if choice in search_functions:
        show_loading_animation()
        steps, result, stats = search_functions[choice](arr.copy(), target, speed)
        navigate_steps(steps, "searching")
        if result != -1:
            print(f"\nTarget {target} found at index {result}")
        else:
            print(f"\nTarget {target} not found")
        print(f"Comparisons: {stats['comparisons']}")
        print(f"Time Complexity: {stats['time_complexity']}")
    else:
        print("Invalid choice!")

def navigate_steps(steps, algorithm_type):
    """Navigate through algorithm steps with back/forward functionality"""
    if not steps:
        print("No steps to display.")
        return
    
    current_step = 0
    total_steps = len(steps)
    
    while True:
        # Display current step
        step = steps[current_step]
        if algorithm_type == "sorting":
            display_array(step['array'], step['highlight_indices'], step['explanation'])
        else:
            display_search(step['array'], step.get('current_index', -1), step.get('target', ''), step.get('explanation', ''))
        
        # Display navigation info
        print(f"\nStep {current_step + 1} of {total_steps}")
        print("Navigation:")
        print("  [Enter] - Next step")
        print("  [b] - Previous step")
        print("  [q] - Quit visualization")
        
        # Get user input
        user_input = input("Your choice: ").strip().lower()
        
        if user_input == '':  # Enter key
            if current_step < total_steps - 1:
                current_step += 1
            else:
                print("\nVisualization complete!")
                break
        elif user_input == 'b':  # Back
            if current_step > 0:
                current_step -= 1
            else:
                print("Already at the first step!")
                time.sleep(1)
        elif user_input == 'q':  # Quit
            print("Exiting visualization...")
            break
        else:
            print("Invalid input! Use Enter, 'b', or 'q'")
            time.sleep(1)

def main():
    while True:
        clear_screen()
        choice = main_menu()
        if choice == '1':
            clear_screen()
            sort_choice = sorting_menu()
            if sort_choice in ['1', '2', '3', '4', '5', '6']:
                arr = get_user_array()
                run_sorting_algorithm(sort_choice, arr)
            else:
                print("Invalid choice!")
        elif choice == '2':
            clear_screen()
            search_choice = searching_menu()
            if search_choice in ['1', '2']:
                arr = get_user_array()
                target = int(input("Enter the target value to search: "))
                speed = validate_speed()
                run_searching_algorithm(search_choice, arr, target, speed)
            else:
                print("Invalid choice!")
        elif choice == '3':
            print("Exiting... Thanks for using the visualizer!")
            break
        else:
            print("Invalid choice!")
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()