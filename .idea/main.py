import random
class Dog:
    def __init__(self, name):
        self.name = name
        self.hun = 50
        self.glad = 10
        self.alive = True
    def run(self):
        print("time to study")
        self.hun -= 3
        self.glad += 3
    def sleep(self):
        print("time to sleep")
        self.glad += 3
        self.hun += 3
    def chill(self):
        self.glad += 5
        self.hun -= 2
    def eat(self):
        self.glad += 1
        self.hun += 5

    def is_alive(self):
        if self.hun < 1:
            self.alive = False
            print("die")
        elif self.glad <= 0:
            print("ahhh i have depresion and die")
            self.alive = False
    def day(self):
        print(f"hungry", {self.hun})
        print(f"gladnes", {self.glad})
    def live(self, day):
        day = "Day"+str(day)+"of"+"live"
        print(f"{day:=^50}")
        cube = random.randint(1,3)
        if cube == 1:
            self.eat()
        if cube == 2:
            self.run()
        if cube == 3:
            self.chill()

        self.day()
        self.is_alive()


rr = Dog(name = "apricot")
for day in range(365):
    if rr.alive == False:
        print(rr.live(day))
        break
    rr.live(day)