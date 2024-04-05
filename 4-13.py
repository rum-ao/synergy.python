import random
n = int(input())
m = int(input())

matrix1=[[random.randint(1, 11) for j in range(n)] for i in range(m)]
for i in range(m):
    print(matrix1[i])
print()

matrix2 = [[ random.randint(1, 11) for j in range(n)] for i in range(m)]
for i in range(m):
    print(matrix2[i])
print()

result = [[matrix1[i][j] + matrix2[i][j]  for j in range
(len(matrix1[0]))] for i in range(len(matrix1))] 
   
for r in result: 
    print(r)
