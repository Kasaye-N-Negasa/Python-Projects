from tabulate import tabulate
print(tabulate(data, headers=col_names, tablefmt="grid", showindex="always"))
    #create data
data = [["Is it mutable?", Yes, Yes, No], 
        ["Can we change the size after creation?", No, Yes, No], 
        ["Can items in the list be changed?", Yes, No, No], 
        ["How many different types of data can be stored?", Four, Five, Four]]
  
#define header names
col_names = ["<>", "Lists", "Arrays", "Tuples"]
  
#display table
print(tabulate(data, headers=col_names, tablefmt="fancy_grid"))
