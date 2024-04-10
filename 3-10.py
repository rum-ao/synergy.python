pets = dict()
name = input("vvedite imya zhivotnogo: ")
vid = input("vvedite vid zhivotnogo: ")
age = int(input("vvedite vozrast zhivotnogo: "))
age_prist = ''
if (age > 4) and (age < 21):
    age_prist = 'let'
else:
    if age%10==1:
        age_prist = 'god'
    elif age%10 < 5:
        age_prist = 'goda'
    else:
        age_prist = 'let'
pet_owner = input("vvedite imya vladeltca zhivotnogo: ")
char = {"Vid pitomca":vid, "Vozrast pitomca":age, "imya vladeltca":pet_owner}
pets[name] = char
pet_name = list(pets.keys())[0]
print(f'Eto {char.get("Vid pitomca")} po klichke "{pet_name}". Vozrast: {char.get("Vozrast pitomca")} {age_prist}. Hozyain: {char.get("imya vladeltca")}.')
##################################################
slovar = dict()
for i in range(10, -5-1, -1):
    slovar[i] = i**i
print(slovar)
