# Base class
class Entity:
    def move(self):
        pass  # Abstract method

# Animal classes
class Cat(Entity):
    def move(self):
        print("Walking gracefully 🐈")

class Bird(Entity):
    def move(self):
        print("Flying elegantly 🐦")

# Vehicle classes
class Car(Entity):
    def move(self):
        print("Driving 🚗")

class Plane(Entity):
    def move(self):
        print("Flying ✈️")

# Demonstrating polymorphism
def demonstrate_movement(entities):
    for entity in entities:
        entity.move()

# Create instances of different entities
entities = [Cat(), Bird(), Car(), Plane()]

# Demonstrate how each entity moves
demonstrate_movement(entities)