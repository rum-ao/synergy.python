n = int(input())
x = set(map(int, input().split()))
print(len(x))
##########################################
x1 = set(map(int, input().split()))
x2 = set(map(int, input().split()))
print (len(x1.intersection(x2)))
##########################################
n1 = set(map(int, input().split()))
x3=set()
for i in n1:
    if i in x3:
        print("YES")
    else:
        print("NO")
    x3.add(i)
