#Nivel 1#
# Step 1: Create an empty tuple
empty_tuple = ()

# Step 2: Create tuples with names of imaginary siblings
sisters = ("Anna", "Maria")
brothers = ("John", "Peter")

# Step 3: Join brothers and sisters tuples and assign it to siblings
siblings = sisters + brothers

# Step 4: Count the number of siblings
print("Number of siblings:", len(siblings))

# Step 5: Add the names of parents to siblings and assign it to family_members
family_members = siblings + ("Father", "Mother")
print("Family members:", family_members)

#Nivel 2#
# Step 1: Unpack siblings and parents from family_members
*siblings_unpack, parents_unpack_1, parents_unpack_2 = family_members
print("Siblings:", siblings_unpack)
print("Parents:", parents_unpack_1, parents_unpack_2)

# Step 2: Create fruits, vegetables, and animal products tuples
fruits = ("Apple", "Banana", "Orange")
vegetables = ("Carrot", "Broccoli", "Spinach")
animal_products = ("Milk", "Eggs", "Cheese")

# Join the three tuples into food_stuff_tp
food_stuff_tp = fruits + vegetables + animal_products
print("Food items (tuple):", food_stuff_tp)

# Step 3: Convert food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print("Food items (list):", food_stuff_lt)

# Step 4: Slice out the middle item or items
middle_index = len(food_stuff_lt) // 2
if len(food_stuff_lt) % 2 == 0:
    middle_items = food_stuff_lt[middle_index - 1: middle_index + 1]
else:
    middle_items = food_stuff_lt[middle_index]
print("Middle items:", middle_items)

# Step 5: Slice out the first three and the last three items
first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]
print("First three items:", first_three)
print("Last three items:", last_three)

# Step 6: Delete food_stuff_tp tuple completely
del food_stuff_tp
# food_stuff_tp is now deleted

# Step 7: Check if an item exists in a tuple
nordic_countries = ("Denmark", "Finland", "Iceland", "Norway", "Sweden")
print("Is 'Estonia' a Nordic country?", "Estonia" in nordic_countries)
print("Is 'Iceland' a Nordic country?", "Iceland" in nordic_countries)