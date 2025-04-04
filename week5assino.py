
class Superhero:
    def __init__(self, name, power, strength):
        self.name = name            
        self._power = power         
        self.__strength = strength  

    def show_identity(self):
        return f"My name is {self.name}, and I use {self._power} to protect the world."

    def display_strength(self):
        return f"My strength level is {self.__strength}."

# Derived class (Inheritance)
class FlyingHero(Superhero):
    def __init__(self, name, power, strength, flight_speed):
        super().__init__(name, power, strength)  
        self.flight_speed = flight_speed         

    # Method overriding (Polymorphism)
    def show_identity(self):
        return f"I am {self.name}, a flying hero with a flight speed of {self.flight_speed} km/h!"

# Encapsulation (Access modifiers demonstration)
class EncapsulatedHero(Superhero):
    def get_power(self):
        return f"My secret power is {self._power}."

    def get_strength(self):
        return f"My private strength is {self._Superhero__strength}." 

# Create objects
basic_hero = Superhero("ShadowKnight", "Shadow Manipulation", 85)
flying_hero = FlyingHero("SkyGuard", "Wind Control", 90, 500)

# Display information
print(basic_hero.show_identity())
print(basic_hero.display_strength())
print(flying_hero.show_identity())
print(flying_hero.display_strength())

# Encapsulation demo
encap_hero = EncapsulatedHero("MysticFlame", "Fire Manipulation", 100)
print(encap_hero.get_power())
print(encap_hero.get_strength())