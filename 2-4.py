a = float(input("Vvedite 1 storonu pryamougolnika: "))
b = float(input("Vvedite 2 storonu pryamougolnika: "))
print(a*b)

a = int(input("Vvedite celoe pyatiznachnoe chislo: "))
ed = a%10
ed1 = a//10
des = a%100
des1 = des//10
sot = a//100
sot1 = sot%10
destis_tis = sot//10
tis = destis_tis%10
destis = sot//100
print (float(((des1**ed)*sot1)//(destis - tis)))
