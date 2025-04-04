# Task 1: Declare an empty list
empty_list = []

# Task 2: Declare a list with more than 5 items
my_list = [1, 2, 3, 4, 5, 6]

# Task 3: Find the length of your list
length = len(my_list)

# Task 4: Get the first item, the middle item, and the last item of the list
first_item = my_list[0]
middle_item = my_list[len(my_list)//2]  # Adjust for even number of items if needed
last_item = my_list[-1]

# Task 5: Declare a list called mixed_data_types
mixed_data_types = ["Mariana", 25, 5.8, "Single", "Basella 130"]

# Task 6: Declare a list variable named it_companies
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# Task 7: Print the list
print(it_companies)

# Task 8: Print the number of companies in the list
print(len(it_companies))

# Task 9: Print the first, middle, and last company
print(it_companies[0], it_companies[len(it_companies)//2], it_companies[-1])

# Task 10: Modify one company in the list
it_companies[0] = "Meta"
print(it_companies)

# Task 11: Add an IT company to it_companies
it_companies.append("Tesla")
print(it_companies)

# Task 12: Insert an IT company in the middle of the list
it_companies.insert(len(it_companies)//2, "Twitter")
print(it_companies)

# Task 13: Change one company's name to uppercase (excluding IBM)
it_companies[1] = it_companies[1].upper()
print(it_companies)

# Task 14: Join the companies with a string '#;&nbsp; '
joined_companies = "#;&nbsp; ".join(it_companies)
print(joined_companies)

# Task 15: Check if a certain company exists
print("Google" in it_companies)

# Task 16: Sort the list using sort() method
it_companies.sort()
print(it_companies)

# Task 17: Reverse the list in descending order
it_companies.reverse()
print(it_companies)

# Task 18: Slice out the first 3 companies
print(it_companies[:3])

# Task 19: Slice out the last 3 companies
print(it_companies[-3:])

# Task 20: Slice out the middle company or companies
middle_start = len(it_companies)//2 - 1
middle_end = len(it_companies)//2 + 1
print(it_companies[middle_start:middle_end])

# Task 21: Remove the first company
it_companies.pop(0)
print(it_companies)

# Task 22: Remove the middle company or companies
middle_index = len(it_companies)//2
it_companies.pop(middle_index)
print(it_companies)

# Task 23: Remove the last company
it_companies.pop(-1)
print(it_companies)

# Task 24: Remove all IT companies
it_companies.clear()
print(it_companies)

# Task 25: Destroy the IT companies list
del it_companies

# Task 26: Join front_end and back_end lists
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
joined_list = front_end + back_end
print(joined_list)

# Task 27: Copy joined_list to full_stack and insert Python and SQL after Redux
full_stack = joined_list.copy()
redux_index = full_stack.index("Redux") + 1
full_stack[redux_index:redux_index] = ["Python", "SQL"]
print(full_stack)