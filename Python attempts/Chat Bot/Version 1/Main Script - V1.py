name = input("What's your name?")
print("Hello, {name}, welcome to ID10T Customer Support.")


def main():
    choice = '0'
    while choice == '0':
        print("Type 1 to VIEW_FAQS ")
        print("Type 2 to ENTER_ERROR_CODE ")
        print("Type 3 to ENTER_SEARCH_QUERY ")
        print("Type 4 to CREATE_TICKET ")
        print("Type 5 to VIEW_TICKET ")
        print("Type 6 to EXIT ")

        choice = input("Please make a choice: ")

        if choice == "1":
            VIEW_FAQS()
        elif choice == "2":
            ENTER_ERROR_CODE()
        elif choice == "3":
            ENTER_SEARCH_QUERY()
        elif choice == "4":
            CREATE_TICKET()
        elif choice == "5":
            VIEW_TICKET()
        elif choice == "6":
            EXIT()
        else:
            print("I don't understand your choice. ")


def VIEW_FAQS():
    with open("FAQs.txt", "r") as file:
        for line in file:
            print(line)
        file.close()
    main()


def ENTER_ERROR_CODE():
    with open("Error_Codes.txt", "r") as file:
        for line in file:
            print(line)
        file.close()
    main()


def ENTER_SEARCH_QUERY():
    with open("data.txt", "r") as file:
        for line in file:
            print(line)
        file.close()
    main()


def CREATE_TICKET():
    File_name = input("Please enter File Name: ")
    with open("data.txt", "w") as file:
        file.write(File_name + "\n")
        file.close()
    main()


def VIEW_TICKET():
    with open("data.txt", "r") as file:
        for line in file:
            print(line)
        file.close()
    main()


def EXIT():
    print("Goodbye!")
    exit()
    main()


main()
