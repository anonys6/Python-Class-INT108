a = (2, 4, 6, 8)
b = (4, 8, 12)

# a[1] = 4.0

c = (7,)

chg_ind_2_of_a = a[0:2] + c + a[3:]

print("Length of a:", len(a))
print("Length of b:", len(b))


print("After chaning element of index 2 of a", chg_ind_2_of_a)