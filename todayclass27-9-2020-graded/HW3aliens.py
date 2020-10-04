# Program is structured wrongly. I don't see if/else chain at all. 
"""
def alien_points(colour):
    if colour == 'green':
        return  5

points = alien_points("green")
print(f"You just earned {points} points for shooting the alien !")

def alien_points(colour):
    if colour == 'red':
        return  10

points = alien_points("red")
print(f"You just earned {points} points for shooting the alien !")
"""

def alien_points(colour):
    if type(colour) == str: 
        if colour.lower() == 'green':
            return  5
        else: 
            return 10
    else: 
        print(f"Invalid input {colour} must be a string")

points = alien_points("green")
print(f"You just earned {points} points for shooting the alien and your color is green!")

points = alien_points("red")
print(f"You just earned {points} points for shooting the alien and your coloer is red !")

points = alien_points("Green") # Code did not account for it. need to check all cases. 
print(f"You just earned {points} points for shooting the alien and your color is green!")


points = alien_points("REd") # Code did not account for it. need to check all cases. 
print(f"You just earned {points} points for shooting the alien and your color is red!")

points = alien_points(101) # Code did not account for it. need to check all cases. 

