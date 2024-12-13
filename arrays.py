# 1.4 Prints some array elements
#
arr = [2, 3, 7, 5, 4]

print(arr)
print('Number of elements:', len(arr))
print('First value:', arr[0])
print('Second value:', arr[1])
print('Last value:', arr[len(arr) - 1])  # Using len(arr) - 1 for the last value
print('Last but one value:', arr[len(arr) - 2])  # Using len(arr) - 2 for the last but one value
print('Sum of the first and last value:', arr[0] + arr[len(arr) - 1])
print('Middle value:', arr[len(arr) // 2])  # Integer division for the middle index

# Print all values separated by a single space
print('All values:', end=' ')
for value in arr:
    print(value, end=' ')

# 1.5

# Initialize the array
arr = [1, 2, 3, 4, 5]

# Print the original array
print("Array:", arr)

# Subtract one from the first element
arr[0] -= 1
print("Array:", arr)

# Increase the last element by 4
arr[len(arr) - 1] += 4
print("Array:", arr)

# Multiply the middle element by 2
arr[len(arr) // 2] *= 2
print("Array:", arr)

# 1.6

def weekday(n):
    weekdays = ["Monday", "Tuesday", "Wednesday",
                "Thursday", "Friday", "Saturday", "Sunday"]
    return weekdays[n - 1]  # Adjust for 0-based indexing

# Print the names of the days for the given day numbers
day_numbers = [1, 4, 7]
for day in day_numbers:
    print(f"Day {day}: {weekday(day)}")

# 1.7
# Prints shopping list
shopping_list = [
   "milk", "bread", "eggs", "butter", "cheese",
   "tomatoes", "potatoes", "carrots", "onions", "garlic"
]

for item in shopping_list:
   print(item)

# 1.8
# List of popular computer games
computer_games = [
   "Minecraft", "Fortnite", "Cyberpunk 2077", "The Witcher 3",
   "League of Legends", "Valorant", "Grand Theft Auto V", 
   "Elden Ring", "Apex Legends", "Call of Duty: Warzone"
]

computer_games.sort()

index = 0

while index < len(computer_games):
    print(f"{index + 1}. {computer_games[index]}")
    index += 1

# 1.9
# Prints vehicle registration numbers from Krakow

polish_license_plates = [
   'KR5233F', 'PO6987E', 'KR16179', 'BI7192L', 'KK12255',
   'WA7930T', 'SK6922I', 'KK61108', 'KR90538', 'BI8052Q',
   'KK54985', 'LU4864U'
]

counter = 1
for car_number in polish_license_plates:
   if car_number.startswith('KR') or car_number.startswith('KK'):
      print(counter, car_number)
      counter += 1

# 1.10
# Prints test statistics

test_results = [
   False, True, False, True, True,
   True, True, False, True, True,
   False, True, True, True, False
]

number_of_questions = len(test_results)

correct_answers = 0
for answer in test_results:
   if answer:
      correct_answers += 1

incorrect_answers = number_of_questions - correct_answers
percentage_correct = (correct_answers / number_of_questions) * 100

print('TEST STATISTICS')
print('===============')
print('Number of questions:', number_of_questions)
print('Number of correct answers:', correct_answers)
print('Number of incorrect answers:', incorrect_answers)
print(f'Percentage of correct answers: {percentage_correct:.2f}%')


# 1.11
# The weather station report

temperatures = [
  3, 7, 1, -2, 6, -4, 5, 1, 2, 3,
  4, -1, 0, 2, -1, -2, 5, -2, 7, 2,
  -1, 4, 1, -4, 2, 3, 6, 7, 5, 7
]

# Number of measurements
measurements = len(temperatures)

# Calculate average temperature
temp_total = 0
for temp in temperatures:
    temp_total += temp
avg_temp = temp_total / measurements

# Calculate min and max temperatures
min_temp = min(temperatures)
max_temp = max(temperatures)

# Calculate number of days with negative temperatures
negative_temp = 0
i = 0
while i < measurements:
    if temperatures[i] < 0:
        negative_temp += 1
    i += 1

# Print the report
print("TEMPERATURE REPORT")
print("Month: March")
print("Number of measurements:", measurements)
print(f"Average temperature in the month: {avg_temp:.2f}")
print("Minimum temperature:", min_temp)
print("Maximum temperature:", max_temp)
print("Number of days with negative temperature:", negative_temp)


# 1.12
# Expense categories and corresponding expenses

categories = ["Food", "Transport", "Rent", "Entertainment"]
expenses = [500, 150, 1000, 200]

# Find the maximum expense
max_expense = max(expenses)

# Find the index of the maximum expense
max_index = expenses.index(max_expense)

# Get the category corresponding to the maximum expense
most_expensive_category = categories[max_index]

print("The most expensive category is:", most_expensive_category)
print("Expense amount:", max_expense)

# 1.13

# Prices of 10 products in the computer store (in currency units)
product_prices = [2999.99, 149.99, 499.99, 89.99, 1199.99, 349.99, 189.99, 99.99, 249.99, 999.99]

# Number of units available for each product
product_quantities = [5, 20, 10, 15, 7, 12, 25, 18, 9, 4]

# Calculate the total value of all the goods available in the store
# zip() function combines the two lists (product_prices and product_quantities) element by element,
# so that each price and its corresponding quantity can be processed together.
total_value = 0
for price, quantity in zip(product_prices, product_quantities):
    total_value += price * quantity

# Print the total value
print("Total value of all goods in the store:", total_value)

# 1.15
# Bubble sort function
def bubble_sort(arr):
    n = len(arr) 
    for i in range(n): 
        for j in range(n - i - 1):  
            if arr[j] > arr[j + 1]:  
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  
    return arr

car_fuel_consumption = [7.2, 6.8, 7.5, 7.0, 7.1, 6.9, 7.3]
bank_transactions = [-150, -20, 300, -45, -60, 500, -120]

# Sorting car fuel consumption
print("Original car fuel consumption:", car_fuel_consumption)
sorted_car_fuel_consumption = bubble_sort(car_fuel_consumption)
print("Sorted car fuel consumption:", sorted_car_fuel_consumption)

# Sorting bank transactions
print("Original bank transactions:", bank_transactions)
sorted_bank_transactions = bubble_sort(bank_transactions)
print("Sorted bank transactions:", sorted_bank_transactions)


# 1.16
# Data collections
distances_traveled = [120, 150, 180, 90, 200, 175, 160]
daily_temperatures = [16, 17, 15, 14, 18, 19, 17, 15, 16, 18]
file_names = ["report.docx", "presentation.pptx", "data.csv", "photo.jpg", "notes.txt",
   "invoice.pdf", "resume.docx", "budget.xlsx", "meeting.mp4", "schedule.pdf"]

# Sort distances_traveled from lowest to highest value
sorted_distances = sorted(distances_traveled)
print("Sorted distances traveled (ascending):", sorted_distances)

# Sort daily_temperatures from highest to lowest value (descending order)
sorted_temperatures_descending = sorted(daily_temperatures, reverse=True)
print("Sorted daily temperatures (descending):", sorted_temperatures_descending)

# Sort file_names in ascending order (alphabetically)
sorted_file_names = sorted(file_names)
print("Sorted file names (alphabetically):", sorted_file_names)

# 2.2
# 3x3 Tic-Tac-Toe board
tic_tac_toe_board = [
   ['X', 'O', 'X'],
   [' ', 'X', 'O'],
   ['O', ' ', 'X']
]

for row in tic_tac_toe_board:
   for cell in row:
      print(cell, end=" ")
   print()  # Moves to the next line after each row

# 2.3

# Weekly expenses for different categories
# [Food, Transport, Utilities]
monthly_expenses = [
   [200, 50, 100],  # Week 1
   [180, 60, 110],  # Week 2
   [220, 55, 105],  # Week 3
   [210, 65, 95]    # Week 4
]

# Initialize totals for categories
total_food = 0
total_transport = 0
total_utilities = 0

# Initialize totals for weeks
week_totals = [0] * 4  # List to hold the total for each week

# Calculate totals for each category and week
for i in range(4):  # Loop over weeks
    total_food += monthly_expenses[i][0]
    total_transport += monthly_expenses[i][1]
    total_utilities += monthly_expenses[i][2]
    week_totals[i] = sum(monthly_expenses[i])

# Print expenses
print('MONTHLY EXPENSES')
print('----------------')
print('Food:', total_food)
print('Transport:', total_transport)
print('Utilities:', total_utilities)

for i in range(4):
    print(f'Week {i + 1}:', week_totals[i])

# Total expenses for the month
total_expenses = total_food + total_transport + total_utilities
print('---------------')
print('TOTAL:', total_expenses)

# 2.4
# Weekly meal plan [Breakfast, Lunch, Dinner] for 7 days
meal_plan = [
   ["Oatmeal", "Grilled Chicken Salad", "Spaghetti"],
   ["Pancakes", "Sandwich", "Steak"],
   ["Smoothie", "Chicken Wrap", "Salmon"],
   ["Eggs", "Pasta", "Soup"],
   ["Toast", "Burrito", "Pizza"],
   ["Cereal", "Salad", "Fish Tacos"],
   ["Bagel", "Rice and Beans", "Stir-fry"]
]

def weekday(n):
   weekdays = ["Monday", "Tuesday", "Wednesday",
      "Thursday", "Friday", "Saturday", "Sunday"]
   return weekdays[n-1]

# Returns a string with day meal names separated by comma
def day_meal_plan(meal_plan, day_number):
   meals = meal_plan[day_number - 1]  # Get meals for the day (day_number is 1-indexed)
   return ", ".join(meals)  # Join the meals into a single string

# Prints weekly meal plan
print("WEEKLY MEAL PLAN\n(Breakfast, Lunch, Dinner)")
print("==========================")

# Loop through each day of the week and print the meals
for day in range(1, 8):
   print(f"{weekday(day)}: {day_meal_plan(meal_plan, day)}")


# 2.5 
# 5x5 cinema seating
# A = Available, B = Booked
cinema_seats = [
   ['A', 'A', 'B', 'A', 'A'],
   ['A', 'B', 'B', 'A', 'A'],
   ['A', 'A', 'A', 'A', 'B'],
   ['B', 'A', 'A', 'A', 'A'],
   ['A', 'B', 'A', 'A', 'A']
]

# Returns the total number of seats
def seats_total(seats):
   return len(seats) * len(seats[0])  # Total seats = rows * columns

# Calculates the number of available seats
def seats_available(seats):
   available = 0
   for row in seats:
      available += row.count('A') 
   return available

# Calculates the number of booked seats
def seats_booked(seats):
   booked = 0
   for row in seats:
      booked += row.count('B')  
   return booked

def seat_status(seats, row, place):
   if seats[row-1][place-1] == 'A':
      return 'Available'
   else:
      return 'Booked'

print('CINEMA INFORMATION TABLE')
print('Total seats:', seats_total(cinema_seats))
print('Seats available:', seats_available(cinema_seats))
print('Seats booked:', seats_booked(cinema_seats))
print('Seat in row 1, place 1:', seat_status(cinema_seats, 1, 1))
print('Seat in row 5, place 5:', seat_status(cinema_seats, 5, 5))
print('Seat in row 3, place 5:', seat_status(cinema_seats, 3, 5))

# 2.6
# Initial matrix
matrix = [
   [0, 0, 0],
   [0, 0, 0],
   [0, 0, 0]
]

# Replace the values of the main diagonal with 1
for i in range(len(matrix)):  # Loop through each row
    matrix[i][i] = 1  # [i][i] - row and column are the same

# Print the modified matrix
for row in matrix:
    print(" ".join(map(str, row)))


# 3.2
import random

# arr1 = [3,7,1,0,4]
arr1 = [3, 7, 1, 0, 4]

# arr2 = [[2,3],[7,1],[0,4]]
arr2 = [[2, 3], [7, 1], [0, 4]]

# arr3 = [7 for i in range(5)]
arr3 = [7 for i in range(5)]

# arr4 = [i for i in range(1,10)]
arr4 = [i for i in range(1, 10)]

# arr5 = [i*2 for i in range(1,10)]
arr5 = [i * 2 for i in range(1, 10)]

# arr6 = [random.randint(1,20) for i in range(10)]
arr6 = [random.randint(1, 20) for i in range(10)]

# arr7 = [[] for i in range(5)]
arr7 = [[] for i in range(5)]

# arr8 = [[1 for i in range(2)] for j in range(4)]
arr8 = [[1 for i in range(2)] for j in range(4)]

# arr9 = [[random.randint(1,20) for i in range(3)] for j in range(5)]
arr9 = [[random.randint(1, 20) for i in range(3)] for j in range(5)]

# Array with values: 4,0,3
arr10 = [4, 0, 3]

# 15-element array filled with zeros
arr11 = [0 for i in range(15)]

# Array with integer values in the range of <1,30>
arr12 = [random.randint(1, 30) for i in range(10)]

# 20-element array filled with 0 or 1 randomly
arr13 = [random.choice([0, 1]) for i in range(20)]

# Two-dimensional array with five rows and two columns filled with False
arr14 = [[False for i in range(2)] for j in range(5)]

# Printing the arrays
print("arr1:", arr1)
print("arr2:", arr2)
print("arr3:", arr3)
print("arr4:", arr4)
print("arr5:", arr5)
print("arr6:", arr6)
print("arr7:", arr7)
print("arr8:", arr8)
print("arr9:", arr9)
print("arr10:", arr10)
print("arr11:", arr11)
print("arr12:", arr12)
print("arr13:", arr13)
print("arr14:", arr14)

# 3.1
# Array containing integers
arr = [34, 7, 19, 4, 21, 8]

# Initialize a counter for even numbers
even_count = 0

# Initialize the index for the while loop
i = 0

while i < len(arr):
    if arr[i] % 2 == 0:  
        even_count += 1  
    i += 1  

print("Number of even values:", even_count)

# 3.2
# Array containing natural numbers
arr = [15, 8, 31, 47, 2, 19]

print("Existed array:", *arr)

print("Reverse array:", end=" ")
for i in range(len(arr)-1, -1, -1): 
    print(arr[i], end=" ")

# 3.3
# Original array
arr = [8, 2, 5, 1, 9]

print("Array:", *arr)

print("2nd power:", end=" ")
for num in arr:
    print(num**2, end=" ")


# 3.4
# Array of numbers
arr = [-15, 8, -31, 47, -2, 19]

# Initialize max and min with the first element in the array
max_num = arr[0]
min_num = arr[0]

for num in arr:
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num

print("Maximum number:", max_num)
print("Minimum number:", min_num)

# 3.5
# Array of values
arr = [15, 8, 31, 47, 2, 19]

total_sum = 0

for num in arr:
    total_sum += num

mean = total_sum / len(arr)

print("Array:", arr)
print("Arithmetic mean:", mean)

# 3.6
# Array of values
arr = [15, 8, 31, 47, 2, 19]

# Initialize variables
total_sum = 0
index = 0

while index < len(arr):
    total_sum += arr[index]
    index += 1

mean = total_sum / len(arr)

print("Array:", arr)
print("Arithmetic mean:", mean)

# 3.7
# List of Polish names
names = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]
longest_name = ""

for name in names:
    if len(name) > len(longest_name):
        longest_name = name

print("Names:", " ".join(names))
print("Longest name:", longest_name)


# 3.8
# Function that returns a string of 'n' asterisks
def star(n):
    return '*' * n

# Array of integers
numbers = [2, 6, 4, 9, 7]

# Iterate through the array and print the number and its graphical representation
for num in numbers:
    print(f"{num}: {star(num)}")


# 3.9
def compare(array1, array2):
    # First, check if lengths are the same
    if len(array1) != len(array2):
        return False
    
    # If lengths are the same, compare element by element
    for i in range(len(array1)):
        if array1[i] != array2[i]:
            return False
    
    return True

# Arrays to compare
arrays = [
    (["water", "book", "sky"], ["water", "book", "sky"]),
    ([True, False], [True, False, True]),
    ([5, 3, 1], [5, 3, 1]),
    ([3, 2, 1], [3, 2])
]

# Compare the arrays and print results
i = 1
for array1, array2 in arrays:
    print(f"Array{i}: {' '.join(map(str, array1))}")
    print(f"Array{i + 1}: {' '.join(map(str, array2))}")
    
    if compare(array1, array2):
        print(f"Comparison: arrays are the same")
    else:
        print(f"Comparison: arrays are different")
    
    print()
    i += 2 

# 3.10
# Define the two arrays
array1 = [4, 36, 12, 28, 9, 44, 5]
array2 = [5, 1, 36]

# Find the numbers in array1 that do not appear in array2
result = [num for num in array1 if num not in array2]

# Print the result
print("Numbers from the first array that do not appear in the second array:")
print(result)

# 3.11
def bubbleSort(arr):
    n = len(arr) 
    for i in range(n):  
        for j in range(n - i - 1): 
            if arr[j] > arr[j + 1]:  
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

array1 = [64, 25, 12, 22, 11]
array2 = [5, 3, 8, 6, 2, 7]
array3 = [20, 5, 8, 15, 3, 12, 6]

sorted_array1 = bubbleSort(array1)
sorted_array2 = bubbleSort(array2)
sorted_array3 = bubbleSort(array3)

print("Sorted Array 1:", sorted_array1)
print("Sorted Array 2:", sorted_array2)
print("Sorted Array 3:", sorted_array3)

# 3.12
def find_unique_elements(arr):
    unique_elements = []
    
    for num in arr:
        # Check if the element occurs only once in the array
        if arr.count(num) == 1:
            unique_elements.append(num)
    
    return unique_elements

arr = [2, 3, 2, 5, 8, 1, 9, 8]
unique_elements = find_unique_elements(arr)

print("Array:", " ".join(map(str, arr)))
print("Unique elements:", " ".join(map(str, unique_elements)))

# 3.13
# Define the function that checks if a number is in the array
def occurs(number, array):
    return number in array  

number = int(input("Enter a number: "))

array = [15, 38, 7, 23, 14]

print(f"Array: {' '.join(map(str, array))}")
if occurs(number, array):
    print(f"Result: number {number} appears in the array")
else:
    print(f"Result: number {number} does not appear in the array")

 # 3.14
 # # Create a tuple containing the word 'computation'
word_tuple = ('computation',)

# Print the type of the tuple
print("Type of variable:", type(word_tuple))

# 3.15
# Define the tuple
tuple1 = (10, 20, 30, 40, 50)

print("Tuple:", tuple1)

reverse_tuple = tuple1[::-1]
print("Reverse order:", reverse_tuple)

# 3.16
# Define the tuple
my_tuple = ("Seven", [10, 20, 30], (5, 15, 25))

print(my_tuple[0])  
print(my_tuple[1][2])  

# 3.17
# Define the tuple
my_tuple = (50, 20, 40, 50, 30, 50)

value_to_count = 50

occurrences = my_tuple.count(value_to_count)

print("Tuple:", my_tuple)
print("Value:", value_to_count)
print("Number of occurrences:", occurrences)


# 3.19
# Define the function to count elements greater than a given value
def count_greater_than(arr, value):
    count = 0
    for num in arr:
        if num > value:
            count += 1
    return count

arr = [4.5, 7.8, 1.2, 3.6, 9.0, 5.3, 6.1]

value = float(input("Enter a value: "))

result = count_greater_than(arr, value)
print(f"The number of elements greater than {value} is: {result}")

# 3.20
# Function to separate even and odd numbers in the array
def separate_even_odd(arr):
    even_numbers = []
    odd_numbers = []
    
    for num in arr:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)
    
    return even_numbers + odd_numbers

arr = [7, 9, 2, 4, 5, 6]
arr = separate_even_odd(arr)

print("arr =", arr)

# 3.21
def is_subset(array1, array2):
    for element in array1:
        if element not in array2:
            return False 
    return True  

# Example arrays
array1 = [3, 5, 7]
array2 = [1, 2, 3, 5, 7, 9]

# Check if array1 is a subset of array2
if is_subset(array1, array2):
    print("Array1 is a subset of Array2.")
else:
    print("Array1 is NOT a subset of Array2.")

#3.22
import random

def rand_elem(array):
    return random.choice(array)

array = [10, 20, 30, 40, 50]

print(rand_elem(array)) 
print(rand_elem(array)) 
print(rand_elem(array))  

#3.25
import matplotlib.pyplot as plt

# Lists to store x and y values
x = []
y = []

# Create x values from -100 to 100
for n in range(-100, 101):
    x.append(n)

# Create corresponding y values for the function f(x) = x^2 - 3
for n in x:
    y.append(n**2 - 3)

# Plot the graph
plt.plot(x, y)

# Show the plot
plt.show()


# 3.26
import math
import matplotlib.pyplot as plt

# Generate x values (angles in degrees from 0 to 360)
x = list(range(361))  # List of angles from 0 to 360 degrees

# Calculate y values (sin(x)) for each x
y = [math.sin(math.radians(n)) for n in x]

# Plot the graph
plt.plot(x, y)

# Show the plot
plt.grid(True)
plt.show()

# 3.27
# Create a 2x4 array
array = [
    [1, 2, 3, 4],
    [5, 6, 7, 8]
]

for row in array:
    print(" ".join(str(x) for x in row))

# 3.28
# Define the 2D array
array = [
    [7, 3, 7, 9, 0],
    [2, 9, 0, 1, 5],
    [3, 8, 6, 4, 7],
    [8, 7, 1, 1, 5]
]

sum_last_column = 0

for row in array:
    # Add the value from the last column (index -1) to the sum
    sum_last_column += row[-1]

print(f"The sum of the values in the last column is: {sum_last_column}")

# 3.29
# Function to create a 2D array of size x by y with values of 0
def create_2d_arr(x, y):
    return [[0 for _ in range(y)] for _ in range(x)]

# Define the dimensions of the 2D array
x = 3  
y = 5 

array = create_2d_arr(x, y)

for row in array:
    print(row)

# 3.30
# Define the number of rows and columns for the multiplication table
rows = 5
cols = 5

table = []

for i in range(1, rows + 1):  # Loop through rows
    row = [] 
    for j in range(1, cols + 1):  # Loop through columns
        row.append(i * j)  
    table.append(row)  
    
for row in table:
    print(" ".join(map(str, row))) 

# 3.31
# Define the array
array = [[-38, 19], [5, 40], [-7, 11], [29, 16]]

smallest = array[0][0]
largest = array[0][0]
smallest_position = (0, 0) 
largest_position = (0, 0)  

# Loop through each row and column
for i in range(len(array)):
    for j in range(len(array[i])):
        # Check if current element is smaller than the smallest
        if array[i][j] < smallest:
            smallest = array[i][j]
            smallest_position = (i, j)  # Update the position of smallest
        # Check if current element is larger than the largest
        if array[i][j] > largest:
            largest = array[i][j]
            largest_position = (i, j)  # Update the position of largest

print(f"Smallest value: {smallest} at row {smallest_position[0]}, column {smallest_position[1]}")
print(f"Largest value: {largest} at row {largest_position[0]}, column {largest_position[1]}")

# 3.32
# Define a 3x5 array
array = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]

def print_array(arr):
    for row in arr:
        print(row)

print("Array before swapping rows:")
print_array(array)

array[0], array[-1] = array[-1], array[0]

print("\nArray after swapping rows:")
print_array(array)

# 3.33
# Define a 3x5 array
array = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]

# Function to print the array in rows and columns format
def print_array(arr):
    for row in arr:
        print(row)

# Print the array before swap
print("Array before swapping columns:")
print_array(array)

# Swap the first and last columns
for row in array:
    row[0], row[-1] = row[-1], row[0]

print("\nArray after swapping columns:")
print_array(array)


# 3.34
def identity_matrix(n):
    # Create a 2D list (matrix) of size n x n filled with zeros
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    
    # Set the diagonal elements to 1
    for i in range(n):
        matrix[i][i] = 1
    
    return matrix

def print_2d_array(matrix):
    # Print each row of the matrix
    for row in matrix:
        print(" ".join(map(str, row)))

sizes = [3, 5, 8]

for size in sizes:
    print(f"Identity Matrix of size {size}:")
    identity = identity_matrix(size)
    print_2d_array(identity)
    print()  # Print an empty line between matrices

# 3.35
def transpose_matrix(m):
    # Transpose the matrix by switching rows and columns
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]

def print_2d_array(matrix):
    # Print each row of the matrix
    for row in matrix:
        print(" ".join(map(str, row)))

# Matrices to be transposed
matrix_a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix_b = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 0]
]

matrix_c = [
    [5, 6, 7, 8]
]

# Print the original and transposed matrices
print("Matrix A (Original):")
print_2d_array(matrix_a)
print("\nMatrix A (Transposed):")
transposed_a = transpose_matrix(matrix_a)
print_2d_array(transposed_a)

print("\nMatrix B (Original):")
print_2d_array(matrix_b)
print("\nMatrix B (Transposed):")
transposed_b = transpose_matrix(matrix_b)
print_2d_array(transposed_b)

print("\nMatrix C (Original):")
print_2d_array(matrix_c)
print("\nMatrix C (Transposed):")
transposed_c = transpose_matrix(matrix_c)
print_2d_array(transposed_c)

# 3.36
def convert_to_1d(arr):
    result = []
    
    for row in arr:
        # Extend the result list by adding each element in the row
        result.extend(row)

    return result

array_a = [
    [2, 3],
    [1, 5]
]

print("1D Array for a):", convert_to_1d(array_a))

array_b = [
    [5, 0, 3, 7, 5],
    [9, 0, 9, 1, 2]
]

print("1D Array for b):", convert_to_1d(array_b))

array_c = [
    [2, 1],
    [3, 5],
    [7, 4],
    [2, 6]
]

print("1D Array for c):", convert_to_1d(array_c))







