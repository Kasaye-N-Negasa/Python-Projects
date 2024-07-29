name = input("What's your name?")
print("Hello, {name}, welcome to ID10T Customer Support.")


def main():
    choice = '0'
    while choice == '0':
        print("Type 1 to VIEW_FAQS ")
        print("Type 2 to ENTER_ERROR_CODE ")
	print("Type 3 to VIEW_ERROR_CODE ")
        print("Type 4 to ENTER_SEARCH_QUERY ")
        print("Type 5 to CREATE_TICKET ")
        print("Type 6 to VIEW_TICKET ")
        print("Type 7 to EXIT ")

        choice = input("Please make a choice: ")

        if choice == "1":
            VIEW_FAQS()
        elif choice == "2":
            ENTER_ERROR_CODE()
	elif choice == "3":
            VIEW_ERROR_CODE()
        elif choice == "4":
            ENTER_SEARCH_QUERY()
        elif choice == "5":
            CREATE_TICKET()
        elif choice == "6":
            VIEW_TICKET()
        elif choice == "7":
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
    with open("error_codes.txt", "w") as file:
        for line in file:
            print(line)
        file.close()
    main()


def VIEW_ERROR_CODE():
    with open("error_codes.txt", "r") as file:
        for line in file:
            print(line)
        file.close()
    main()


def ENTER_SEARCH_QUERY():
    with open("search_query.txt", "w") as file:
        for line in file:
            print(line)
        file.close()
    main()


def CREATE_TICKET():
    ticket_content = input("Please enter the ticket content: ")
    with open("ticket.txt", "w") as file:
        file.write(ticket_content + "\n")
        file.close()
    main()


def VIEW_TICKET():
    with open("ticket.txt", "r") as file:
        for line in file:
            print(line)
        file.close()
    main()


def EXIT():
    print("Goodbye, {name}, thank you for using ID10T Customer Support.")
    main()


main()
