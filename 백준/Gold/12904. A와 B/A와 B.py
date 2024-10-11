a = input()
b = input()
while (b != a):
    if (len(b) == 0):
        print("0")
        exit()
    if (b[-1] == 'A'):
        b = b[:-1]
    elif (b[-1] == 'B'):
        b = b[::-1]
        b = b[1:]
    else:
        print("0")
        exit()
print("1")