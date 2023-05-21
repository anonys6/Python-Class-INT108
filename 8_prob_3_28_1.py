from tkinter import Y


p = int (input ("Enter dollars: "))
r = float (input ("Enter rate of intrest: "))
y = int (input ("For how many years: "))

fd = p * (1 + (0.01 * r)) * y

print ("You will get", fd, "dollars")