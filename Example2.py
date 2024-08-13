class Vehicles:
    def __init__(self, make, model, year, price):
        self.make = make
        self.model = model
        self.year = year
        self.price = price

    def Origin_check(self):
        if self.make == "ford" or self.make == "chevy" or self.make == "tesla":
            return "American made"
        else:
            return "imported"

    def model_c(self):
        return self.model

    def year_check(self):
        if self.year >= 2000:
            return "Car is from 21st century"
        else:
            return "Car is older"

    def budget(self, maxbudget):
        if self.price > maxbudget:
            return "not in budget"
        else:
            return "with in budget"


class Style(Vehicles):
    def __init__(self,make,model,year,price, num_of_doors):
        super().__init__(make,model,year,price)
        self.num_of_doors = num_of_doors

    def style_check(self):
        if self.num_of_doors == 4:
            return "Family car"
        elif self.num_of_doors == 2:
            return "sports car"
        else:
            "not specified yet"


vehicle1 = Vehicles('tesla', "v1", 2001, 30000)
# print(vehicle1.Origin_check())
# print(vehicle1.budget(20000))
#
# car = Style("toyota","camry",2002,30000,4)
# print(car.year_check())
# print(car.style_check())
sports_car=Style("supra","vs",1999,15999,2)
print(sports_car.year_check())
print(sports_car.model_c())
print(sports_car.budget(30000))
print(sports_car.style_check())
