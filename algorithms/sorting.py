import time
from utils.visualizer import display_array

def bubble_sort(arr):
    steps = []
    comparisons = 0
    swaps = 0
    n = len(arr)
    for i in range(n):
        step_swaps = 0
        for j in range(0, n - i - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
                step_swaps += 1
                steps.append({
                    'array': arr.copy(),
                    'highlight_indices': [j, j + 1],
                    'explanation': f"Pass {i + 1}: Compared {arr[j + 1]} and {arr[j]}, swapped because {arr[j + 1]} > {arr[j]}."
                })
        if step_swaps == 0:
            steps.append({
                'array': arr.copy(),
                'highlight_indices': [],
                'explanation': f"Pass {i + 1}: No swaps needed, array is sorted."
            })
            break
        else:
            steps.append({
                'array': arr.copy(),
                'highlight_indices': [],
                'explanation': f"Pass {i + 1} complete: Largest element moved to position {n - i - 1}."
            })
    return steps, {"comparisons": comparisons, "swaps": swaps, "time_complexity": "O(n^2)"}

def selection_sort(arr):
    steps = []
    comparisons = 0
    swaps = 0
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            comparisons += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            swaps += 1
            steps.append({
                'array': arr.copy(),
                'highlight_indices': [i, min_idx],
                'explanation': f"Iteration {i + 1}: Found minimum {arr[i]} at index {min_idx}, swapped with element at index {i}."
            })
        else:
            steps.append({
                'array': arr.copy(),
                'highlight_indices': [i],
                'explanation': f"Iteration {i + 1}: Element {arr[i]} at index {i} is already the minimum."
            })
    return steps, {"comparisons": comparisons, "swaps": swaps, "time_complexity": "O(n^2)"}

def insertion_sort(arr):
    steps = []
    comparisons = 0
    swaps = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            comparisons += 1
            arr[j + 1] = arr[j]
            swaps += 1
            j -= 1
        arr[j + 1] = key
        steps.append({
            'array': arr.copy(),
            'highlight_indices': [j + 1],
            'explanation': f"Iteration {i}: Inserted {key} at index {j + 1} by shifting larger elements right."
        })
    return steps, {"comparisons": comparisons, "swaps": swaps, "time_complexity": "O(n^2)"}

def merge_sort(arr):
    steps = []
    stats = {"comparisons": 0, "swaps": 0, "time_complexity": "O(n log n)"}
    def merge(arr, l, m, r):
        left = arr[l:m + 1]
        right = arr[m + 1:r + 1]
        i = j = 0
        k = l
        while i < len(left) and j < len(right):
            stats["comparisons"] += 1
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
                stats["swaps"] += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
        steps.append({
            'array': arr.copy(),
            'highlight_indices': [l, r],
            'explanation': f"Merged subarrays from indices {l} to {m} and {m + 1} to {r}."
        })
    
    def merge_sort_helper(arr, l, r):
        if l < r:
            m = (l + r) // 2
            merge_sort_helper(arr, l, m)
            merge_sort_helper(arr, m + 1, r)
            merge(arr, l, m, r)
    
    merge_sort_helper(arr, 0, len(arr) - 1)
    return steps, stats

def quick_sort(arr):
    steps = []
    stats = {"comparisons": 0, "swaps": 0, "time_complexity": "O(n log n) average"}
    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            stats["comparisons"] += 1
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                stats["swaps"] += 1
                steps.append({
                    'array': arr.copy(),
                    'highlight_indices': [i, j],
                    'explanation': f"Partitioning with pivot {pivot}: Compared {arr[j]} with pivot, swapped with index {i}."
                })
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        stats["swaps"] += 1
        steps.append({
            'array': arr.copy(),
            'highlight_indices': [i + 1, high],
            'explanation': f"Partition complete: Pivot {pivot} placed at index {i + 1}."
        })
        return i + 1
    
    def quick_sort_helper(arr, low, high):
        if low < high:
            pi = partition(arr, low, high)
            quick_sort_helper(arr, low, pi - 1)
            quick_sort_helper(arr, pi + 1, high)
    
    quick_sort_helper(arr, 0, len(arr) - 1)
    return steps, stats

def heap_sort(arr):
    steps = []
    stats = {"comparisons": 0, "swaps": 0, "time_complexity": "O(n log n)"}
    def heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n:
            stats["comparisons"] += 1
            if arr[left] > arr[largest]:
                largest = left
        if right < n:
            stats["comparisons"] += 1
            if arr[right] > arr[largest]:
                largest = right
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            stats["swaps"] += 1
            steps.append({
                'array': arr.copy(),
                'highlight_indices': [i, largest],
                'explanation': f"Heapifying: Swapped {arr[i]} with {arr[largest]} at index {largest} to maintain heap property."
            })
            heapify(arr, n, largest)
    
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
        steps.append({
            'array': arr.copy(),
            'highlight_indices': [i],
            'explanation': f"Building max heap: Heapified subtree rooted at index {i}."
        })
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        stats["swaps"] += 1
        steps.append({
            'array': arr.copy(),
            'highlight_indices': [0, i],
            'explanation': f"Extracted max element {arr[i]} to position {i}, heapifying root."
        })
        heapify(arr, i, 0)
    return steps, stats