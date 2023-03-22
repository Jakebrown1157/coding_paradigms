class Podracer: 
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price

    def repair(self):
        self.condition = 'repaired'

class Anakins_Pod(Podracer):
    def __init__(self, max_speed, condition, price):
        super.__init__(max_speed, condition, price)

    def boost(self):
        self.max_speed * 2

class SebulbasPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)

    def flame_jet(self, otherPod):
        otherPod.condition = 'trashed'

# encapsulation, we bundle the arguments within the class podracer and then pass them to another class
# abstractions not really used to hide info
# inheritance is used to give the new classes the same methods and variable by passing the old class in as an argument   SebulbasPod(Podracer):
# polymorphism __init__ and super() are used in most classes 

# using classes is pretty simple when thinking about adding a bunch of podracers to a race where each one needs to have different methods and functions. 
# However in this case where only 2 podracers were created it would've been simpler to take the functional route. 

# OOP helped because the different methods could be tacked on to the newer classes making it pretty easy to create new podracers with special methods like flame_jet or boost