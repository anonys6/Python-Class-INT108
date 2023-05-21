mNum = input("Enter your mobile number: ")
if (mNum.isdigit() and len(mNum) 10):
    if(mNum[0] >= 6 and mNum[0] <= 9):
        print("Mobile number is valid")
    else:
        print("Mobile number is not starting with 6, 7, 8 or 9")
else:
    print("Mobile number is not valid")
