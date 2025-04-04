Enter your age: 25
You are old enough to learn to drive.
Output:
Enter your age: 25
You need 3 more years to learn to drive.

Enter your age: 25
You are 5 years older than me.
Enter number one: 4
Enter number two: 3
4 is greater than 3
age = int(input("Enter your age: "))
if age >= 18:
    print("You are old enough to learn to drive.")
else:
    years_left = 18 - age
    print(f"You need {years_left} more year{'s' if years_left > 1 else ''} to learn to drive.")
my_age = 25  # Replace with your actual age
your_age = int(input("Enter your age: "))

if your_age > my_age:
    difference = your_age - my_age
    print(f"You are {difference} year{'s' if difference > 1 else ''} older than me.")
elif your_age < my_age:
    difference = my_age - your_age
    print(f"I am {difference} year{'s' if difference > 1 else ''} older than you.")
else:
    print("We are the same age!")
a = int(input("Enter number one: "))
b = int(input("Enter number two: "))

if a > b:
    print(f"{a} is greater than {b}")
elif a < b:
    print(f"{a} is smaller than {b}")
else:
    print(f"{a} is equal to {b}")

#Level 2#
80-100, A
70-89, B
60-69, C
50-59, D
0-49, F
