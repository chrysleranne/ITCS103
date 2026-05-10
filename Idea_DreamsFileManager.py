file_name = "dreamss.txt"

while True:
    print("\n\t****************************************************")
    print("\t*              DREAMS FILE MANAGER                 *")
    print("\t****************************************************")
    print("\t* Please select from the options :                 *")
    print("\t*                                                  *")
    print("\t* 1 . Read inspiring messages                      *")
    print("\t* 2 . Add a new inspiring message                  *")
    print("\t* 3 . Rewrite the entire file                      *")
    print("\t* 4 . Exit Program                                 *")
    print("\t*                                                  *")
    print("\t****************************************************")


    choice = input("Enter your choice: ")

    if choice == "1":

        file = open(file_name, "r")

        print("\n\t┌───────────────────────────────────────────┐")
        print("\t│         INSPIRING MESSAGES MENU           │")
        print("\t└───────────────────────────────────────────┘\n")

        print(file.read())

        file.close()


    elif choice == "2":
        print("\n\t┌───────────────────────────────────────────┐")
        print("\t│        ADD NEW INSPIRING MESSAGE          │")
        print("\t└───────────────────────────────────────────┘\n")

        message = input("Enter your inspiring message: ")

        file = open(file_name, "a")
        file.write(message + "\n")
        file.close()

        print("Message added successfully.")

    elif choice == "3":
        print("\n\t┌───────────────────────────────────────────┐")
        print("\t│          REWRITE FILE CONTENTS            │")
        print("\t└───────────────────────────────────────────┘\n")

        print("\tWarning: This will overwrite the file.")
        confirm = input("\tType YES to continue: ")

        if confirm == "YES":
            new_message = input("\n\tWrite your new set of inspiring messages:\n")

            file = open(file_name, "w")
            file.write(new_message + "\n")
            file.close()

            print("\t\nFile has been overwritten.")

        else:
            print("\n\tOperation is cancelled:>")

    elif choice == "4":
        print("\n\tThank you for using Idea's Dream File Manager! :)")
        break

    else:
        print("\tInvalid choice. Try again.")