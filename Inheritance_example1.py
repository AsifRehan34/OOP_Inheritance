class Animal:
    def __init__(self,name,pet):
        self.name=name
        self.pet=pet
        self.sound=None
    def speak(self):
        print(self.sound)
    def pet_info(self):
        print(self.name)
        print(self.pet)
        print(self.sound)
class Fish(Animal):
    def swim(self):
        if self.sound==None:
            print("i am a fish and i dont have a sound")
        else:
            print("you can't be a fish")
    def Ocean(self,ocean):
        self.ocean=ocean
        print(f"{self.name} is a {self.pet} who live in {self.ocean}")
myfish=Fish('memo','fish')
myfish.speak()
myfish.pet_info()
myfish.swim()
oc=input("Enter the name of the ocean: ")
myfish.Ocean(oc)