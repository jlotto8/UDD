'''
This is an exercise in class and API design. For this exercise, please use this CSV file containing information on various animals.

Setup
- An `Animal` has the following properties:
    - Name
    - Number of legs
    - Sound that it makes

classes are the defnition what each animal looks like; objects can be created- which are instances of the class

- A `Monster` is created from two different `Animals` with the same number of legs: one for the head and one for the body.
- A `Monster` has the following properties:
    - Name (the combination of the names of the head and body)
    - Number of legs
    - `Animal` head
    - `Animal` body
    - Sound that it makes (the combination of the sounds of its `Animal` head and body)

Tasks

We are going to design some classes and functions to create and interact with `Monster`s. The below descriptions are using generic pseudocode — the class and function signatures will look different in the specific programming language you are using.

The class and function definitions below are not fully specified — you will need to make some decisions about how they should work to be useful to someone who would use your code in their own projects.

Please implement the following:
- An `Animal` class
    - Example constructor call: `Animal(name: "Octopus", numLegs: 8, sound: "Burble")`
- A `Monster` class, that creates a `Monster` from an `Animal` head and an `Animal` body
    - Example constructor call: `Monster(head: Animal(Octopus), body: Animal(Scorpion))`
        - `Monster.name` → `OctopusScorpion`
        - `Monster.sound` → `BurbleHiss` 
    - Your code should ensure that we can only create a `Monster` with the head and body of two different `Animals`, who have the same number of legs.
- A function `createAllMonsters` that takes as input a number of legs and returns an array of all `Monsters` that can be made with that number of legs. A `Monster` with `Animal` A head and `Animal` B body is distinct from a `Monster` with `Animal` B head and `Animal` A body. Please use the animals.txt file linked at the beginning of this problem.
    - Example function call: `createAllMonsters(8)` → `[Monster(OctopusScorpion), Monster(ScorpionOctopus)]`
    - The crux of this function is: how do we produce all of the combinations of heads and bodies for animals with a given number of legs?
- A function `getRandomMonster` that takes as input a number of legs and returns a random Monster with that number of legs.
    - Example function call: `getRandomMonster(8)` → `Monster(OctopusScorpion)`
    - This function should call your `createAllMonsters` function
'''
"""
write a file that will read the csv and create 
later- functions will use the class
create an animal class, loop the csv, and make each 'animal' an object of the class

class Complex:
    def __init__(self, realpart, imagpart):  <--- init every time an object is created
        self.r = realpart
        self.i = imagpart
x = Complex(3.0, -4.5)
x.r, x.i
(3.0, -4.5)
AnimalName,AnimalType,NumLegs,Sound
"""
import csv

def main():
    create_animals()

class Animal:
    def __init__(self, animal_name, animal_type, num_legs, sound) -> None:
        self.animal_name = animal_name
        self.animal_type = animal_type
        self.num_legs = num_legs
        self.sound = sound

        # print(animal_name, animal_type, num_legs, sound)
    
def create_animals():

    with open('animals.csv', newline='') as csvfile:
        animal_reader = csv.DictReader(csvfile, delimiter=',')

        for row in animal_reader:
            if row['AnimalName']:
                animal_name = Animal(row['AnimalName'], animal_type = row['AnimalType'], num_legs = row['NumLegs'], sound = row['Sound'] ) #  Animal creates a function call for the init method 
            
if __name__=="__main__": 
    main() 

# review classes, OOP, objects