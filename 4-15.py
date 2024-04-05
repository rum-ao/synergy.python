class Transport():

   def __init__(self, name, max_speed, mileage):
       self.name = name
       self.max_speed = max_speed
       self.mileage = mileage

       
x = Transport("KAMAZ", 350, 1000)
print(f'{x.name} skorost: {x.max_speed} probeg: {x.mileage}')
#############################################################

class Transport():

   def __init__(self, name, max_speed, mileage):
       self.name = name
       self.max_speed = max_speed
       self.mileage = mileage
       
   def seating_capacity(self, capacity):
       return f"vmestimost odnogo avtobusa {self.name}  {capacity} passazhirov"

class Autobus(Transport):
    capacity = 50
    
    def seating_capacity(self, capacity):
        print(f'vmestimost odnogo avtobusa {self.name} {capacity} passazhirov')

x = Autobus('kamaz', 200, 100)
x.seating_capacity(50)
