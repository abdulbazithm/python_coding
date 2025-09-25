import os

# File Handling Menu-Driven Program
while True:
    print("Welcome to File Handling!!")
    print("_" * 50)
    print("Choose an Option")
    print("1. Create a File   2. Append   3. Rewrite")
    print("4. Read/View       5. Delete a File")
    print("Press 0 to Exit..")

    opt = int(input("\nEnter an Option: "))

    # ✅ Option 1: Create a new file
    if opt == 1:
        name = input("\nEnter Your Good Name: ")
        file = name + ".txt"

        if os.path.exists(file):
            print("Error: This User is already Registered!")
            print("Create a New User File..")
        else:
            mail = input("\nEnter Your Mail Id: ")
            ph = int(input("\nEnter Your 10 digit Mobile Number: "))
            ad = input("\nEnter Your Address: ")

            # Write details into the new file
            with open(file, "w") as f:
                f.write(f"Name: {name}\n")
                f.write(f"Address: {ad}\n")
                f.write(f"Mail Id: {mail}\n")
                f.write(f"Mobile: {ph}\n")

            print("\nFile created Successfully! Contents:")
            print("_" * 35)
            with open(file, "r") as f:
                print(f.read())

    # ✅ Option 2: Append new details into existing file
    elif opt == 2:
        name = input("\nEnter Your Name: ")
        file = name + ".txt"

        while True:
            new = input("\nWhat you want to add (e.g. Hobby, Skills, Place): ")
            entry = input(f"Enter your {new}: ").strip()

            with open(file, "a") as f:
                f.write(f"{new}: {entry}\n")

            confirm = input("\nPress 'y' to add more or 'n' to cancel: ").lower()
            if confirm != "y":
                break

        print("\nDetails Added! New Contents:")
        print("_" * 35)
        with open(file, "r") as f:
            print(f.read())

    # ✅ Option 3: Rewrite (overwrite file completely)
    elif opt == 3:
        name = input("\nEnter Your Name: ")
        file = name + ".txt"

        new = input("\nWhat you want to rewrite? ")
        entry = input("Enter your Entry: ")

        with open(file, "w") as f:
            f.write(f"{new}: {entry}\n")

        print("\nRewrite Done! New Contents: ")
        print("_" * 35)
        with open(file, "r") as f:
            print(f.read())

    # ✅ Option 4: Read/View file
    elif opt == 4:
        try:
            name = input("\nEnter Your Name: ")
            file = name + ".txt"

            print("\nHere is Your File Contents: ")
            print("_" * 35)
            with open(file, "r") as f:
                print(f.read())

        except FileNotFoundError:
            print("Error: There is no such file")

    # ✅ Option 5: Delete file
    elif opt == 5:
        name = input("\nEnter Your Name: ")
        file = name + ".txt"

        confirm = input("\nPress 'y' to Confirm Deletion or 'n' to Cancel: ").lower()

        if confirm == "y":
            if os.path.exists(file):
                os.remove(file)
                print("File deleted successfully.")
            else:
                print("Error: No such User file to Delete")
        else:
            print("Cancelled!")

    # ✅ Exit program
    elif opt == 0:
        print("\nSee You Again! Have a Great Day...")
        break

    # ✅ Invalid option
    else:
        print("\nChoose only from the above Options")
