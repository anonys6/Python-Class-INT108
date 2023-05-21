from string import *
vow = 'AEIOU'
for i in ascii_uppercase:
    if (i in vow):
        print(i, "is vower")
    else:
        print(i, "is consonant")