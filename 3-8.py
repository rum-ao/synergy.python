n = int(input())
massive1 = []
for i in range(n):
    a = int(input())
    massive1.append(a)
print(*massive1[::-1])
##################################
n = int(input())
massive2 = list(map(int, input().split()))
new_massive2 = [massive2[-1]] + massive2[:-1]
print(*new_massive2)
