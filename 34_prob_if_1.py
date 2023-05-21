correctPass = "password"

for i in range (0, 3):
    askPass = input("Enter the password: ")
    if (askPass == correctPass):
        print("Your have successfully logged in.")
        break

    elif (askPass != correctPass):
        print("Incorrect Password!\n")
    if (i == 2):
        print("You have been denied access.")
        break

