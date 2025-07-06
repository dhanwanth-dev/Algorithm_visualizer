from utils.visualizer import display_search
import time

def linear_search(arr, target, speed):
    steps = []
    comparisons = 0
    for i in range(len(arr)):
        comparisons += 1
        steps.append({
            'array': arr.copy(),
            'current_index': i,
            'target': target,
            'explanation': f"Checking index {i}: {arr[i]} {'==' if arr[i] == target else '!='} {target}"
        })
        if arr[i] == target:
            steps.append({
                'array': arr.copy(),
                'current_index': i,
                'target': target,
                'explanation': f"Found target {target} at index {i}!"
            })
            return steps, i, {"comparisons": comparisons, "time_complexity": "O(n)"}
    
    steps.append({
        'array': arr.copy(),
        'current_index': -1,
        'target': target,
        'explanation': f"Target {target} not found in the array."
    })
    return steps, -1, {"comparisons": comparisons, "time_complexity": "O(n)"}

def binary_search(arr, target, speed):
    steps = []
    comparisons = 0
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        comparisons += 1
        
        if arr[mid] == target:
            steps.append({
                'array': arr.copy(),
                'current_index': mid,
                'target': target,
                'explanation': f"Found target {target} at index {mid}! Range: [{left}, {right}]"
            })
            return steps, mid, {"comparisons": comparisons, "time_complexity": "O(log n)"}
        elif arr[mid] < target:
            steps.append({
                'array': arr.copy(),
                'current_index': mid,
                'target': target,
                'explanation': f"Checking index {mid}: {arr[mid]} < {target}, search right half. Range: [{left}, {right}]"
            })
            left = mid + 1
        else:
            steps.append({
                'array': arr.copy(),
                'current_index': mid,
                'target': target,
                'explanation': f"Checking index {mid}: {arr[mid]} > {target}, search left half. Range: [{left}, {right}]"
            })
            right = mid - 1
    
    steps.append({
        'array': arr.copy(),
        'current_index': -1,
        'target': target,
        'explanation': f"Target {target} not found in the array."
    })
    return steps, -1, {"comparisons": comparisons, "time_complexity": "O(log n)"}