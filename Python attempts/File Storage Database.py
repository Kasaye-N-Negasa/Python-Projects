def main():
    choice ='0'
    while choice =='0':
        print("Main Choice: Select 1 of 4 choices ")
        print("Type 1 to Create File ")
        print("Type 2 to Locate & View File Data ")
        print("Type 3 to Locate & Updata File Data ")
        print("Type 4 to Locate & Delete File Data ")

        choice = input ("Please make a choice: ")

        if choice == "1":
            Create_File()
        elif choice == "2":
            Locate_and_View_File_Data()
        elif choice == "3":
            Locate_and_Updata_File_Data()
        elif choice == "4":
            Locate_and_Delete_File_Data()
        else:
            print("I don't understand your choice. Please select 1 of 4 choices: Type 1 to Create File, Type 2 to Locate & View File Data, Type 3 to Locate & Updata File Data, or Type 4 to Locate & Delete File Data ")

def Create_File():
    name = input("Please enter File Name: ")
    with open("data.txt", "w") as file:
        file.write(name + "\n")
        file.close()
    main()

def Locate_and_View_File_Data():
    with open("data.txt", "r") as file:
        for line in file:
            print(line)
        file.close()
    main()

def Locate_and_Updata_File_Data():
    with open("data.txt", "r") as file:
        for line in file:

    main()

def Locate_and_Delete_File_Data():
    with open("data.txt", "r") as file:
        for line in file:

    main()

main()
