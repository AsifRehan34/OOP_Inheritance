from time import sleep
class Agents:
    def __init__(self,name,health,car):
        self.name=name
        self.health=health
        self.car=car
    def Agent_info(self):
        print("Your name is :",self.name)
        print("your healt is: ",self.health)
        print("Your car is: ",self.car)
class Spy(Agents):
    def __init__(self,name,health,car,agency,location):
        super().__init__(name,health,car)
        self.agecy=agency
        self.location=location
        self.killed=False
    def attack(self,bad_guy):
        if bad_guy.health>0:
            bad_guy.health-=20
            print(f"the updated health of {self.name} is: ",self.health)
        elif bad_guy.health<=0:
            self.killed=True
            print("Enemy killed")

james_bond=Spy("James bond",100,"porche","isi","pakistan")
james_bond.Agent_info()
ethan_hunt=Spy("Ethan",60,"ferrari","raw","india")
ethan_hunt.Agent_info()
sleep(5)
while ethan_hunt.health>0:
    james_bond.attack(ethan_hunt)
    ethan_hunt.attack(james_bond)
    sleep(2)

