# MyArrays.py module

# Function to return the second largest element in an array
def second_largest(arr):
    # Remove duplicates by converting to a set and then back to a list
    unique_arr = list(set(arr))
    
    # If there are less than 2 unique elements, return None
    if len(unique_arr) < 2:
        return None
    
    # Sort the array in descending order and return the second largest
    unique_arr.sort(reverse=True)
    return unique_arr[1]

# Function to return the difference between the largest and smallest values in an array
def diff_largest_smallest(arr):
    largest = max(arr)
    smallest = min(arr)
    return largest - smallest

# Function to return the median of numbers in an array
def median(arr):
    # Sort the array first
    arr.sort()
    
    n = len(arr)
    # If the number of elements is odd, the median is the middle element
    if n % 2 == 1:
        return arr[n // 2]
    # If the number of elements is even, the median is the average of the two middle elements
    else:
        mid1, mid2 = arr[n // 2 - 1], arr[n // 2]
        return (mid1 + mid2) / 2

# Function to return the smallest and largest values in an array as a tuple
def smallest_largest(arr):
    return (min(arr), max(arr))

# Function to return array elements as a string, separated by the minus sign
def array_to_string(arr):
    return "-".join(map(str, arr))
