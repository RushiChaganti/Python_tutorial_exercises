# This is allright. But better make it as a function. 
"""
age = 16

if age < 2:
    print("You're a baby!")
elif age < 4:
    print("You're a toddler!")
elif age < 13:
    print("You're a kid!")
elif age < 20:
    print("You're a teenager!")
elif age < 65:
    print("You're an adult!")
else:
    print("You're an elder!")
"""

def type_of_person(age):
    if age < 2:
        return "baby"
    elif age < 4:
        return "toddler!"
    elif age < 13:
        return "kid!"
    elif age < 20:
        return "teenager!"
    elif age < 65:
        return "adult!"
    else:
        return "elder!"

# Now the tests. 
person = type_of_person(2)    
print(f"You're a {person}!")

person = type_of_person(2)    
print(f"You're a {person}!")


person = type_of_person(2)    
print(f"You're a {person}!")

person = type_of_person(3)    
print(f"You're a {person}!")

person = type_of_person(12)    
print(f"You're a {person}!")

person = type_of_person(13)    
print(f"You're a {person}!")

person = type_of_person(19)    
print(f"You're a {person}!")

person = type_of_person(22)    
print(f"You're a {person}!")

person = type_of_person(25)    
print(f"You're a {person}!")

person = type_of_person(40)    
print(f"You're a {person}!")

person = type_of_person(44)    
print(f"You're a {person}!")

person = type_of_person(45)    
print(f"You're a {person}!")

person = type_of_person(64)    
print(f"You're a {person}!")

person = type_of_person(65)    
print(f"You're a {person}!")

person = type_of_person(71)    
print(f"You're a {person}!")
