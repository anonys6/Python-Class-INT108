mNum = input("Enter your mobile number: ")
if (mNum.isdigit() and len(mNum)== 10):
#    if(int(mNum[0]) >= 6 and int(mNum[0]) <= 9):
    if(int(mNum[0]) == 6 or int(mNum[0]) == 7 or int(mNum[0]) == 8 or int(mNum[0]) == 9):
        print("Mobile number is valid")
    else:
        print("Mobile number is not starting with 6, 7, 8 or 9")
else:
    print("Mobile number is not valid")