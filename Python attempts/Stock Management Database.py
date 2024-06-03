def main():
    choice ='0'
    while choice =='0':
        print("Main Choice: Choose 1 of 4 choices")
        print("Choose 1 for Add new products")
        print("Choose 2 for Update Stock Level")
        print("Choose 3 for View Stock Level")
        print("Choose 4 to exit")

        choice = input ("Please make a choice: ")

        if choice == "4":
            quit
        elif choice == "3":
            view_stock()
        elif choice == "2":
            update_stock()
        elif choice == "1":
            add_stock()
        else:
            print("I don't understand your choice.")
            
def add_stock():
    name = input("Please enter the name of the product: ")
    with open("data.txt", "w") as file:
        file.write(name + "\n")
        file.close()
    main()
def view_stock():
    with open("data.txt", "r") as file:
        for line in file:
            print(line)
        file.close()
    main()

main()
