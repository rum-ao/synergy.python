import collections

def faktorial(x):
    a = 1
    for i in range(2, x+1):
        a *= i
    return a
    
def spisok_faktorial(x):
    spisok = [faktorial(x)]
    for i in range(x-1, 0, -1):
        spisok.append(faktorial(i))
    print(spisok)

spisok_faktorial(6)
######################################################

pets = {
    1:
        {
            "Barsik": {
                "vid": "kot",
                "vozrast": 9,
                "vladelec": "Lesha"
            },
        },
    2:
        {
            "Muhtar": {
                "vid": "dog",
                "vozrast": 12,
                "vladelec": "Sasha"
            },
        },
}

def get_suffix(age):
    suffix = ''
    if age%10 == 2 or age%10 == 3 or age%10 == 4:
        suffix = 'goda'
    elif age%10 == 1:
        suffix = 'god'
    else:
        suffix = 'let'
    return suffix



def create():
    last = collections.deque(pets, maxlen=1)[0]

    name = input("vvedite imya: ")
    vid = input("vvedite vid: ")
    age = int(input("vvedite vozrast: "))
    pet_owner = input("vvedite imya vladelca: ")
    
    pet = {name:{"vid":vid, "vozrast":age, "vladelec":pet_owner}}
    pets[last+1] = pet



def read(x):
    pet_name = list(pets[x].keys())[0]
    pet_char = list(pets[x].values()) 
    vid = pet_char[0]['vid']
    vozrast = pet_char[0]['vozrast']
    vladelec = pet_char[0]['vladelec']
    print(f'Eto {vid} po klichke "{pet_name}". Vozrast: {vozrast} {get_suffix(vozrast)}. Hozyain: {vladelec}.')




def update(a, b, c):       
    if b == "vid":
        pet_char = list(pets[a].values())
        pet_char[0]['vid'] = c
    elif b == "vozrast":
        pet_char = list(pets[a].values())
        pet_char[0]['vozrast'] = c
    elif b == "vladelec":
        pet_char = list(pets[a].values())
        pet_char[0]['vladelec'] = c
        



def delete(x):
    del pets[x]


command = ''
while(command != 'stop'):
    command = input("Vvedite create, read, update ili delete: ")
    if command == "create":
        create()
    elif command == "read":
        x = int(input("vvedite nomer: "))
        read(x)
    elif command == "update":
        a = int(input("vvedite nomer "))
        b = input("chto pomenyat? vid vvozrast vladelec ")
        c = input("na chto pomenat? ")
        update(a, b, c)
    elif command == "delete":
        x = int(input("vvedite nomer "))
