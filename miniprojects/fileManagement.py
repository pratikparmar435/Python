import os

def createFile(filename):
    try:
        with open(filename,'x') as f:
            print(f"File name {filename}: Created successfully!")
    except FileExistsError:
        print(f"File name {filename} already exist!")
    except Exception as E:
        print("An error occurred!")
    
def viewAllFiles():
    files = os.listdir()
    if not files:
        print("No files found!")
    else:
        print("Files in directory!")
        for file in files:
            print(file)

def deleteFile(filename):
    try:
        os.remove(filename)
        print(f"{filename} has been deleted successfully!")
    except FileNotFoundError:
        print("File not found!")
    except Exception as e:
        print("An error occurred!")
    
def readFile(filename):
    try:
        with open(filename,'r') as f:
            content = f.read()
            print(f"Content of '{filename}':\n{content}")
    except FileNotFoundError:
        print("File not found!")
    except Exception as e:
        print("An error occurred!")

def editFile(filename):
    try:
        with open(filename,"a") as f:
            content = input("Enter a data to file = ")
            f.write(content + '\n')
            print(f"content added to file {filename} successfully!")
    except FileNotFoundError:
        print("File not found!")
    except Exception as e:
        print("An error occurred!")

def main():
    while True:
        print("File Management system")
        print("1. Create a new file")
        print("2. View all files")
        print("3. Delete a file")
        print("4. Read a file")
        print("5. Edit a file")
        print("6. Exit")
        
        choice = input("Enter your choice number = ")
        if choice == '1':
            filename = input("Enter file name = ")
            createFile(filename)
        elif choice == '2':
            viewAllFiles()
        elif choice == '3':
            filename = input("Enter file name to delete = ")
            deleteFile(filename)
        elif choice == '4':
            filename = input("Enter file name to read = ")
            readFile(filename)
        elif choice == '5':
            filename = input("Enter file name to edit = ")
            editFile(filename)
        elif choice == '6':
            print("Exiting the program...")
            break
        else:
            print("Invalid choice!")
main()
            