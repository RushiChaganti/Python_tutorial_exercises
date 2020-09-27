#list of people who are invited for travelling for ladakh

#my list
people_travelling= [ "viswanadh", "shyam", "prasanna"]
guest = people_travelling[0]
print("I would like to invite you for travelling " + guest)

guest= people_travelling[1]
print("I would like to invite you for travelling  " + guest)

guest = people_travelling[2]
print("I would like to invite you for travelling " + guest)

# Adding some people using insert and append

people_travelling.insert(0, "prasad")
people_travelling.insert(1, "sandeep")
people_travelling.append("rushi")

guest= people_travelling[0]
print("I would like to invite you for travelling " + guest)


guest= people_travelling[1]
print("I would like to invite you for travelling " + guest)

guest= people_travelling[5]
print("I would like to invite you for travelling " + guest)

print(people_travelling)

# I found that there is less money but i can take two of you

guest=people_travelling[0]
print(" I found that there  is less money but i can take two of you " + guest)

guest=people_travelling[1]
print(" I found that there  is less money but i can take two of you " + guest)

guest=people_travelling[2]
print("I found that there is less money but i can take two of you " + guest)

guest=people_travelling[3]
print("I found that there is less money but i can take two of you " + guest)

guest=people_travelling[4]
print("I found that there is less money but i can take two of you " + guest)

guest=people_travelling[5]
print("I found that there is less money but i can take two of you " + guest)


#removing some people uisng pop
guest = people_travelling.pop(0)
print("Sorry that I can't invite you for travelling " + guest)
guest = people_travelling.pop(1)
print("Sorry that I can't invite you for travelling " + guest)
guest = people_travelling.pop(2)
print("Sorry that I can't invite you for travelling " + guest)
guest = people_travelling.pop(2)
print("Sorry that I can't invite you for travelling " + guest)

#inviting the other two people 
guest = people_travelling[0]
print(" You are still invited for the travelling " + guest)

guest = people_travelling[1]
print(" You are still invited for the travelling " + guest)

del people_travelling[0]
print(people_travelling)
del people_travelling[0]
print(people_travelling)

