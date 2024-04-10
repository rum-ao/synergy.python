class Kassa():
    cash = 10000

    def __init__(self, cash):
        self.cash = cash
     
    def top_up(self, x):
        self.cash += x
       
    def count_1000(self):
        print(self.cash//1000)
        
    def take_away(self, x):
        if x > self.cash:
            print('ne hvataet deneg')
        else:
            self.cash -= x
            
kassa = Kassa(3000)

kassa.top_up(10)
print(kassa.cash)

kassa.count_1000()

kassa.take_away(10)
print(kassa.cash)

###################################################################

class Cherepaha():
    def __init__(self, x, y, s):
        self.x = x
        self.y = y
        self.s = s
        
    def go_up(self):
        self.y += self.s
        
    def go_down(self):
        self.y -= self.s
        
    def go_left(self):
        self.x -= self.s
        
    def go_right(self):
        self.x += self.s
        
    def evolve(self):
        self.s += 1
        
    def degrade(self):
        if self.s - 1 <= 0:
            print("oshibka")
        else:
            self.s -= 1
        
    def count_moves(self, x2, y2):
        dx = abs(x2 - self.x)
        dy = abs(y2 - self.y)
        return min(dx, dy) // self.s + max(dx, dy) % self.s
    
cherep = Cherepaha(0, 0, 1)

print(cherep.count_moves(3,4))

cherep.degrade()
