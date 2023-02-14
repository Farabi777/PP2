class Living:
    legs = 4
    tail = 1
    def __init__(self, color):
        self.color = color 
    def giveVoice(self):
        print(self.legs, self.tail, self.color)

class Animal(Living):

    def __init__(self, color, voice):
        self.voice = voice
        super().__init__(color)

    def giveVoice(self):
        print(self.legs, self.tail, self.color, self.voice)
    
    def setter(self, name):
        self.name = name
    
    def getter(self):
        return self.name

class Cat(Animal):
    def __init__(self, color, voice, breed):
        super().__init__(color, voice)
        self.breed = breed
        
        
    def giveVoice(self):
        print(self.legs, self.tail, self.voice, self.color, self.breed)

p1 = Animal("WOOF!!!", "GRAY")
p1.setter("KOWKA")
p1.giveVoice()
print(p1.getter())

p1 = Cat("WHITE", "MEOW", "DOMASHNIY")
p1.giveVoice()
    