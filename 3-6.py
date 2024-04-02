n = int(input())
col = 0
zero = 0
while (col<n):
    col+=1
    a = int(input())
    if a == 0:
        zero+=1
print(zero)

x = int(input())
col = 0
for i in range(1, x+1):
    if x%i==0:
        col+=1
print(col)

a = int(input())
b = int(input())
c=[]
for i in range(a,b+1):
    if i%2==0:
        c.append(i)
print(*c)
