class Bichon:
    

    species = "dog"


    def __init__(self, name, age):
        self.name = name
        self.age = age




bluy = Bichon("Bluy", 10)
wolfy = Bichon("Wolfy", 15)

print("Bluy is a {}".format(bluy.species))
print("wolfy is also a {}".format(wolfy.species))
print()

print("{} is {} years old".format( bluy.name, bluy.age))
print("{} is {} years old".format( wolfy.name, wolfy.age))
