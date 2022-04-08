mainPassword= "try254"
q= False

while True:
    mainif= input("Enter the main password: ")
    
    if mainif == "q":
        break
    
    if mainif == "mainPassword":
        q=True
        
    else:
        print("Invalid Password.")
        
    while q:
        answer= input("Would you like to add, delete, view or q? ")
        
        if answer == "q":
            break
        if answer == "add":
            name= input("Enter your account name: ")
            password= input("Password: ")
            with open("passwords.txt", "a") as f:
                f.write(name + " " + password + "\n")
        if answer == "view":
            with open ("password.txt", "r") as f:
                for line in f.readlines():
                    print(line)
             
    