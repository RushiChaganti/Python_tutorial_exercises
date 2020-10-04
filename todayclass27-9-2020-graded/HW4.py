# structure is correct but did not invoke for other coloers. 
def alien_colour(colour): # Modified colour to see if it takes of all the cases. 
    if type(colour) == str:
        if colour.lower() == 'green': # validate if it is string or not
            print(f"You just earned 5 points  for shooting the alien! ")
        elif colour.lower() == 'yellow':
            print(f"You just earned 10 points for shooting the alien! ")
        else:
            print(f"You just earned 15 points for shooting the alien! ")
    else: 
        print(f"colour {colour} must be of type string")

appropriate_colour = alien_colour("red")
# Added more test cases bottom for covering all the colours
appropriate_colour = alien_colour("green")
appropriate_colour = alien_colour("yellow")

appropriate_colour = alien_colour("GrEEn")
appropriate_colour = alien_colour(10)


        
        
 
