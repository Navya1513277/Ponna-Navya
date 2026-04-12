# # Create an empty list
# lst = []

# # -------- CREATE LIST --------
# n = int(input("Enter number of elements: "))

# for i in range(n):
#     element = int(input("Enter element: "))
#     lst = lst + [element]   # using concatenation instead of append

# print("List after creation:", lst)


# # -------- APPEND ELEMENT --------
# new_element = int(input("Enter element to append: "))
# lst = lst + [new_element]   # manual append

# print("List after appending:", lst)


# # -------- REMOVE ELEMENT --------
# remove_element = int(input("Enter element to remove: "))
# new_list = []

# found = False
# for i in lst:
#     if i == remove_element and not found:
#         found = True   # skip only first occurrence
#     else:
#         new_list = new_list + [i]

# lst = new_list
# print("List after removal:", lst)



# # Geometric Mean using User Input (No Methods)
# Ex-1:
# # Step 1: Read number of elements
# n = int(input("Enter number of elements: "))
# # Step 2: Initialize product
# product = 1
# # Step 3: Read elements and multiply
# print("Enter the elements:")
# for i in range(n):
#     value = float(input())
#     product = product * value
# # Step 4: Calculate geometric mean
# geometric_mean = product ** (1 / n)
# # Step 5: Display result
# print("Geometric Mean:", geometric_mean)

# Ex-2
n = int(input("Enter number of elements: "))
data=[]
product=1
for i in range(n):
    value=float(input(f"enter elements{i+1}: "))
    product=product*value
gm=product**(1/n)
print("Geometric mean: ",gm)    