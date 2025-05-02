#lesson 5 

#example 1
# Sum numbers from 1 to 100
total: int = 0
for i in range(1, 101):
    total += i
print("Sum of numbers from 1 to 100:", total)
     

     #example 2
     # Find factors of a number
num: int = 24
factors = []
for i in range(1, num + 1):
    if num % i == 0:
        factors.append(i)
print(f"Factors of {num}: {factors}")
     
     #lesson 6# Create a phonebook
phonebook: dict = {
    "Alice": "123-456-7890",
    "Bob": "987-654-3210",
    "Charlie": "555-555-5555"
}

# Add a new contact
phonebook["David"] = "111-222-3333"

# Search for a contact
name: str = input("Enter a name to search: ")
if name in phonebook:
    print(f"{name}'s phone number is {phonebook[name]}.")
else:
    print(f"{name} is not in the phonebook.")

    #lesson 7

    my_set:  set = {1,2,3, "Hello! World", 4,5,6}
my_set2: set = {1,2,3, "Hello! World", 8,9}
my_set3: set = {1,2,3, "Hello! World", 77}

print("difference()           = ", my_set.difference(my_set2, my_set3)) #Returns a set containing the difference between two or more sets
print("intersection()         = ", my_set.intersection(my_set2, my_set3))#Return a set that contains the items that exist in both set
print("union()                = ", my_set.union(my_set2, my_set3))#Return a set that contains all items from both sets, duplicates are excluded:
print("symmetric_difference() = ", my_set.symmetric_difference(my_set2))#One argument only, #Return a set that contains only unique items from both sets

#my_set = {55,66}

print("isdisjoint()           = ", my_set.isdisjoint(my_set2))#Return True if no items in set x is present in set y

my_set2 = {1,2,3, "Hello! World"}
print("issuperset()           = ", my_set.issuperset(my_set2))#Return True if all items in set x are present in set y
print("issubset()             = ", my_set2.issubset(my_set))
     

