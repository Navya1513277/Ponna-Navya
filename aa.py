import os
def create_file():
    filename = input("Enter file name: ")
    with open(filename, 'w') as f:
        print("File created successfully.")
def write_file():
    filename = input("Enter file name: ")
    with open(filename, 'w') as f:
        data = input("Enter content to write: ")
        f.write(data)
        print("Data written successfully.")
def read_file():
    filename = input("Enter file name: ")
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            print("\nFile Content:")
            print(f.read())
    else:
        print("File does not exist.")
def append_file():
    filename = input("Enter file name: ")
    with open(filename, 'a') as f:
        data = input("Enter content to append: ")
        f.write("\n" + data)
        print("Data appended successfully.")
def delete_file():
    filename = input("Enter file name: ")
    if os.path.exists(filename):
        os.remove(filename)
        print("File deleted successfully.")
    else:
        print("File not found.")
def rename_file():
    filename=input("Enter file name: ")
    if os.path.exists(filename)  :
        newFile=input("Ente new file name: ")
        if os.path.exists(newFile):
            print("New name imported")
        else:
            os.rename(filename,newFile)
            print("Rename successfully")
    else:
        print("File not found")
def replace_file():
    filename=input("Enter file name: ")
    if os.path.exists(filename):
        x=input("Enter new content: ")
        with open(filename,'w')as file:
            f.write(x)
            print("File replaced")
    else:
        print("file does not exit")                                  
while True:
    print("\n--- File Handling Application ---")
    print("1. Create File")
    print("2. Write File")
    print("3. Read File")
    print("4. Append File")
    print("5. Delete File")
    print("6. Rename File")
    print("7. Replace File")
    print("8. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        create_file()
    elif choice == '2':
        write_file()
    elif choice == '3':
        read_file()
    elif choice == '4':
        append_file()
    elif choice == '5':
        delete_file()
    elif choice=='6':
        rename_file()
    elif choice=='7':
        replace_file()        
    elif choice == '8':
        print("Exiting program...")
        break
    else:
        print("Invalid choice!")