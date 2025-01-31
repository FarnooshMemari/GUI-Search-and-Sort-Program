# Name: Farnoosh Memari
# Date: 10/10/2024
# CRN: 10235
# Class name: CIS 226 - Advanced Python Programming
# Estimated time: 6 hours


import tkinter as tk
from tkinter import messagebox

# Global variable to count swaps. The swaps are any movement of the array elements
swap_count = 0

def do_merge(array1, array2):
    """
    Merges the two sorted arrays into one sorted array
    Args:
    array1 (list): The first sorted sublist.
    array2 (list): The second sorted sublist.
    Returns:
    list: the merged sorted array.

    Time complexity: O(n), where n is the total number of elements in both arrays.
    """

    global swap_count
    merged = []
    i = 0
    j = 0
    while i < len(array1) and j < len(array2):
        if array1[i] <= array2[j]:
            merged.append(array1[i])
            i += 1
        else:
            merged.append(array2[j])
            j += 1
        # Increment swap count for each move
        swap_count += 1

    # Adding the rest of the elements from array1 or array2
    merged.extend(array1[i:])
    merged.extend(array2[j:])
    swap_count += len(array1[i:]) + len(array2[j:])  # Add remaining elements as swaps

    return merged

def merge_sort(array, start=None, end=None):
    """
    Performs the merge sort on the array and count the number of swaps.
    Args:
    array (list): The array to be sorted.
    start (int): The starting index of the subarray (default: None).
    end (int): The ending index of the subarray (default: None).
    Returns:
    list: Sorted subarray.

    O(n log n), n is the number of elements in the array.
    """
    if start is None:
        start = 0
    if end is None:
        end = len(array) - 1
    if end - start <= 0:
        return array[start:end + 1]  # There is nothing to sort
    elif end - start == 1:
        if array[start] > array[start + 1]:
            array[start], array[start + 1] = array[start + 1], array[start]
            global swap_count
            swap_count += 1
        return array[start:end + 1]
    else:
        middle = (start + end) // 2
        left_sorted = merge_sort(array[start:middle + 1])
        right_sorted = merge_sort(array[middle + 1:end + 1])
        merged = do_merge(left_sorted, right_sorted)
        array[start:end + 1] = merged
        return array[start:end + 1]

def binary_search(array, target):
    """
    Performs a binary search to find the target in the array that is sorted.
    Args:
    array (list): The sorted array to search in.
    target (int): The integer value to search for.
    Returns:
    tuple: Index of the target and number of steps taken in the search. If the target doesn't exist it returns -1 and the number of steps.

    O(log n), n is the number of elements in the array.
    The array will be divided in half during the search every time.
    """
    low = 0
    high = len(array) - 1
    steps = 0
    while low <= high:
        steps += 1
        mid = (low + high) // 2
        if array[mid] == target:
            return mid, steps
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1, steps

# GUI Part
def search_and_sort():
    """
    Gets the user input, perform sorting and searching and shows the results.

    This function retrieves the input from the user in the format of comma-separated integers.
    Performs Merge Sort to sort the list, and uses Binary Search to find a target integer.
    The number of swaps during sorting and steps during searching are displayed in a message box.
    """
    global swap_count
    swap_count = 0  # Resets swap count for each time we click on sort and search

    # Gets the list of numbers and the target from the user
    input_numbers = entry_numbers.get()
    target = entry_target.get()
    numbers = []
    # Converts string to list of integers. Shows a messagebox if the user input a wrong fromat of list
    try:
        for number in input_numbers.split(','):
            numbers.append(int(number.strip()))
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid list of comma-separated integers.")
        return

    # Sorts numbers using Merge Sort
    sorted_numbers = merge_sort(numbers.copy())

    # Searches for the target using Binary Search
    try:
        target = int(target)
        index, steps = binary_search(sorted_numbers, target)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid integer for the search target.")
        return

    # Displays the results
    result_text = "Sorted List: {}".format(sorted_numbers)
    result_text += "\nNumber of element movements during sorting: {}".format(swap_count)
    if index != -1:
        result_text += "\nTarget {} found at index {} in {} steps.".format(target, index, steps)
    else:
        result_text += "Target {} not found. Search took {} steps.".format(target, steps)
    messagebox.showinfo("Search & Sort Output", result_text)

# GUI
root = tk.Tk()
root.title("Search & Sort")

# GUI layout
label_numbers = tk.Label(root, text="Enter the comma-separated integers:")
label_numbers.pack()

entry_numbers = tk.Entry(root, width=50)
entry_numbers.pack()

label_target = tk.Label(root, text="Enter the target integer to search for:")
label_target.pack()

entry_target = tk.Entry(root, width=20)
entry_target.pack()

button_sort_search = tk.Button(root, text="Sort & Search", command=search_and_sort)
button_sort_search.pack()

# Runs the GUI application

if __name__ == '__main__':
    # Runs the GUI application
    root.mainloop()
