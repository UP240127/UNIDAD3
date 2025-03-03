
# Variables in Python

first_name = 'Asabeneh'
last_name = 'Yetayeh'
country = 'Finland'
city = 'Helsinki'
age = 250
is_married = True
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
    'firstname':'Asabeneh', 
    'lastname':'Yetayeh', 
    'country':'Finland',
    'city':'Helsinki'
    }

# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

# Declaring multiple variables in one line

first_name, last_name, country, age, is_married = 'Asabeneh', 'Yetayeh', 'Helsink', 250, True

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)

#Excersise 2

#2.1

print(type(first_name))
print(type(last_name))
print(type(country))
print(type(city))
print(type(age))
print(type(is_married))
print(type(skills))
print(type(person_info))

#2.2 - 2.3

print(len(first_name))
print(len(last_name))

#Excersise 2.4

print(len(first_name) > len(last_name))
print(len(first_name) < len(last_name))
print(len(first_name) == len(last_name))
print(len(first_name) != len(last_name))
print(len(first_name) >= len(last_name))
print(len(first_name) <= len(last_name))

#Excersise 2.5

num_one = 5
num_two = 4

#Excersise 6 - 11
Total= int(num_one + num_two)
Difference= int(num_one - num_two)
Product= int(num_one * num_two)
Division= int(num_one / num_two)
Remainder= int(num_one % num_two)
Exp= int(num_one ** num_two)
Floor_division= int(num_one // num_two)

print('Total:', Total)
print('Difference:', Difference)
print('Product:', Product)
print('Division:', Division)
print('Remainder:', Remainder)
print('Exp:', Exp)
print('Floor division:', Floor_division)

#Excersise 12

Radius= int(30)
Area_of_circule= int(3.14 * Radius ** 2)  
Circum_of_circule= int(2 * 3.14 * Radius)
print('Area of a circle:', Area_of_circule)
print('Circumference of a circle:', Circum_of_circule)

#Excersise 13

print("\nUser Information:")
print(f"First Name: {first_name}")
print(f"Last Name: {last_name}")
print(f"Country: {country}")
print(f"Age: {age}")

#Excersise 14

help('keywords')