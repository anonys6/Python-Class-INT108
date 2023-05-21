def getSortedNumber(n):
# Convert to equivalent string
    number = str(n)

    # Sort the string
    number = ''.join(sorted(number))
    # Convert to equivalent integer
    number = int(number)
    # Return the integer
    return number


# Driver Code
n = 666665445556

print(getSortedNumber(n))