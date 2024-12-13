# Import MyArrays module
import myarrays

# Given sequence of numbers
numbers = [7, 3, 8, 5, 2]

# Calculate and print the results
print("Numbers:", ", ".join(map(str, numbers)))
print("Second largest number:", myarrays.second_largest(numbers))
print("Median:", myarrays.median(numbers))
smallest, largest = myarrays.smallest_largest(numbers)
print(f"Smallest and largest number: {smallest},{largest}")
print("Numbers as a string:", myarrays.array_to_string(numbers))
