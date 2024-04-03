stroka1 = input()
if stroka1[::-1] == stroka1:
    print("yes")
else:
    print("no")
#######################################
stroka2 = input()
while "  " in stroka2:
    stroka2 = stroka2.replace("  ", " ")
print(stroka2)
