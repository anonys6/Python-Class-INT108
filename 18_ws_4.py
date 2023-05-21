subtotal = float (input ("Enter subtotal and gratuity rate: "))
gRate = float (input())

g = gRate / subtotal
total = g + subtotal

print("The gratuity is", g, "and the total is", total)