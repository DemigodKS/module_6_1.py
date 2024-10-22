
class Animal:
    #в случае с p3
    #alive = False
    alive = True
    fed = False
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        if  food.edible:
            #в случае с p3
            #self.fed = False
            self.fed = True
            print(f'{self.name} сьел {food.name}')
        else:
            print(f'{self.name} не стал есть {food.name}')
            #self.alive = True

class Plant:
    edible = False
    def __init__(self, name):
        self.name = name

class Mammal(Animal):
    pass
class Predator(Animal):
    pass
class Flower(Plant):
    # в случае с p3
    #edible = True
    pass
class Fruit(Plant):
    edible = True


a1 = Predator('Fox')
a2 = Mammal('Dog')
p1 = Flower('Tulip')
p2 = Fruit('Banana')
p3 = Flower('Poisonous berry')

print(a1.name)
print(p1.name)
print()

a1.eat(p1)
print(f'{a1.name} - живая:', a1.alive)
print(f'{a1.name} - сыта:', a1.fed)
print()
a2.eat(p2)
print(f'{a2.name} - живая:', a2.alive)
print(f'{a2.name} - сыта:', a2.fed)
print()

#a1.eat(p3)
#print(f'{a1.name} - живая:', a1.alive)
#print(f'{a1.name} - сыта:', a1.fed)


