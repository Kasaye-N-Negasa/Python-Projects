def main():
    choice ='0'
    while choice =='0':
        print("Please choose 1 of 4 colours: ")
        print("Type 1 for Red ")
        print("Type 2 for Yellow ")
        print("Type 3 for Green ")
        print("Type 4 for Blue ")

        choice = input ("Please make a choice: ")

        if choice == "1":
            print("You chose Red ")
            print(random.choice(Colour_List))
        elif choice == "2":
            print("You chose Yellow ")
            print(random.choice(Colour_List))
        elif choice == "3":
            print("You chose Green ")
            print(random.choice(Colour_List))
        elif choice == "4":
            print("You chose Blue ")
            print(random.choice(Colour_List))
        else:
            print("I don't understand your choice. Please choose 1 of 4 colours: Type 1 for Red, Type 2 for Yellow, Type 3 for Green, or Type 4 for Blue ")

def Colour_List():["Red","Yellow","Green","Blue"]
main()
