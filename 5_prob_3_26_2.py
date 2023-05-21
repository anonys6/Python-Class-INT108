hour = int(input("Enter hours: "))
min = int (input ("Enter minutes: "))
sec = int(input("Enter seconds: "))

inSecs = (hour * 3600) + (min * 60) + sec

print(hour, "hours,", min, "minutes and", sec, "seconds in seconds is", inSecs)