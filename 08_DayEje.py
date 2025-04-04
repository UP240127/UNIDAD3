# Step 1: Create an empty dictionary called dog
dog = {}

# Step 2: Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'Buddy'
dog['color'] = 'Brown'
dog['breed'] = 'Labrador'
dog['legs'] = 4
dog['age'] = 5

# Step 3: Create a student dictionary and add various keys
student = {
    'first_name': 'John',
    'last_name': 'Doe',
    'gender': 'Male',
    'age': 21,
    'marital_status': 'Single',
    'skills': ['Python', 'JavaScript'],
    'country': 'Mexico',
    'city': 'Aguascalientes',
    'address': '123 Main Street'
}

# Step 4: Get the length of the student dictionary
length_of_student_dict = len(student)
print("Length of student dictionary:", length_of_student_dict)

# Step 5: Get the value of skills and check the data type
skills = student['skills']
print("Skills:", skills)
print("Data type of skills:", type(skills))  # Should be <class 'list'>

# Step 6: Modify the skills values by adding one or two skills
student['skills'].extend(['React', 'SQL'])
print("Updated skills:", student['skills'])

# Step 7: Get the dictionary keys as a list
keys_list = list(student.keys())
print("Dictionary keys:", keys_list)

# Step 8: Get the dictionary values as a list
values_list = list(student.values())
print("Dictionary values:", values_list)

# Step 9: Change the dictionary to a list of tuples using _items()_ method
items_list = list(student.items())
print("List of tuples:", items_list)

# Step 10: Delete one of the items in the dictionary
del student['marital_status']
print("After deleting marital_status:", student)

# Step 11: Delete one of the dictionaries
del dog
print("Dog dictionary deleted.")
