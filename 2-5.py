a = int(input("Vvedite celoe chislo: "))
if a == 0:
   print("Nulevoe chislo")
elif a > 0 and a % 2 == 0:
   print("Polozhitel'noe chetnoe chislo")
elif a < 0 and a % 2 == 0:
   print("Otricatel'noe chetnoe chislo")
else:
   print("Chislo ne yavlyaetsya chetnim")
#################################################
word = (input("Vvedite slovo: ")).lower()
vowels = "aeiuy"
count_vowels = 0
count_consonants = 0
for i in range(0, len(word)):
    if word[i] in vowels:
        count_vowels += 1
    else:
       count_consonants += 1
print(count_vowels)
print(count_consonants)
print(f'a = {"False" if word.count("a") == 0 else word.count("a")}, e = {"False" if word.count("e") == 0 else word.count("e")}, i = {"False" if word.count("i") == 0 else word.count("i")}, o = {"False" if word.count("o") == 0 else word.count("o")}, y = {"False" if word.count("y") == 0 else word.count("y")}, u = {"False" if word.count("u") == 0 else word.count("u")}')
