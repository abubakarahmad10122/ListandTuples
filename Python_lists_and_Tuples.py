''' Task 1: Daily Study Planner (Lists)
Objective

Practice list methods and indexing.

Instructions
Create a list of 7 study subjects.
Print all the subjects.
Insert "Computer Science" at the 3rd position.
Remove one subject of your choice.
Replace the last subject with "English Grammar".
Reverse the list.
Sort the list alphabetically.
Check whether "Mathematics" exists in the list.
Print the final study plan. '''

subjects=["Geography","Urdu","Math","Science","Gernal Knowledge","History","English"]

print(subjects)

subjects.insert(2, "Computer Science")

subjects.remove("Science")

subjects.index("English")

print("\n")

subjects.reverse()

subjects.sort()

print(subjects)

print("\n")

'''
Task 2: Country Information (Tuples)
Objective

Practice tuple creation, indexing, slicing, counting, and finding elements.

Instructions
Create a tuple containing the following countries:
Pakistan
China
Turkey
Japan
Canada
Germany
Australia
Print the complete tuple.
Display the first and last country.
Print the first four countries using slicing.
Count how many times Pakistan appears in the tuple.
Find the index of Japan.
Print the total number of countries stored in the tuple.
Try changing one country in the tuple and observe what happens. Write a short note explaining why the change is not allowed.
'''

Countries=("Pakistan","China","Turkey","Japan","Canada","Germany","Australia")

print(Countries)

print("\n")

print(Countries[:4])

print(Countries.count("Pakistan"))

print(Countries.index("Japan"))

print(len(Countries))
