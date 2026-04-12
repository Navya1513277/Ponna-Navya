# Creating a file:

# file = open("example.txt", "w")
# file.write("Hello, this is a new file!")
# file.close()

# # Reading a file:

# file = open("example.txt", "r")
# content = file.read()
# print(content)
# file.close()

# Writing to a file:


# file = open("example.txt", "w")
# file.write("This will overwrite previous content.")
# file.close()

# Appending to a file:

# file = open("example.txt", "a")
# file.write("\nAdding new content without deleting old data.")
# file.close()

# Reading line by line:

# file = open("example.txt", "r")
 
# for line in file:
#     print(line)
# file.close()

# Using "with" statement:(auto closes file)

# with open("example.txt", "r") as file:
#     content = file.read()
#     print(content)

# Checking if file exist:(before opening )

# import os
# if os.path.exists("example.txt"):
#     file = open("example.txt", "r")
#     print(file.read())
#     file.close()
# else:
#       print("File does not exist.")

# Deleting a file:

# import os
# if os.path.exists("example.txt"):
#     os.remove("example.txt")
#     print("File deleted successfully.")
# else:
#     print("File not found.")

# Creating a file only doesnot exist('x'mode):

# try:
#     file = open("newfile.txt", "x")
#     file.write("This file is created.")
#     file.close()
# except FileExistsError:
#     print("File already exists.")
    
# Read and write:
    
# file = open("demo.txt", "r+")
# print("Before writing:", file.read())  
# file.seek(0)  
# file.write("Updated content!")  
# file.close()

# Write and read:

# file = open("demo.txt", "w+")
# file.write("New data written!")  
# file.seek(0)  
# print("After writing:", file.read())  
# file.close()

