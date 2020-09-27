#list of people who are invited for dinner

#my list
people_dinner = [ "viswanadh", "shyam", "prasanna"]

guest = people_dinner[0]
print("i would like to invite you for dinner " + guest)

guest= people_dinner[1]
print("i would like to invite you for dinner " + guest)

guest = people_dinner[2]
print("i would like to invite you for dinner " + guest)

people_dinner.insert(0, "prasad")
people_dinner.insert(1, "sandeep")
people_dinner.append("rushi")


guest= people_dinner[0]
print("i would like to invite you for dinner " + guest)


guest= people_dinner[1]
print("i would like to invite you for dinner " + guest)

guest= people_dinner[5]
print("i would like to invite you for dinner " + guest)

print(people_dinner)

#i found that the dinning table is not ariving on time and i have space for only two guests

guest=people_dinner[0]
print("i found that the dining table is not arriving on time and i have space for only two guests" + guest)

guest=people_dinner[1]
print("i found that the dining table is not arriving on time and i have space for only two guests" + guest)

guest=people_dinner[2]
print("i found that the dining table is not arriving on time and i have space for only two guests" + guest)

guest=people_dinner[3]
print("i found that the dining table is not arriving on time and i have space for only two guests" + guest)

guest=people_dinner[4]
print("i found that the dining table is not arriving on time and i have space for only two guests" + guest)

guest=people_dinner[5]
print("i found that the dining table is not arriving on time and i have space for only two guests" + guest)


#removing some people uisng pop
guest = people_dinner.pop(0)
print("sorry that i can't invite you for dinner " + guest)
guest = people_dinner.pop(1)
print("sorry that i can't invite you for dinner " + guest)
guest = people_dinner.pop(2)
print("sorry that i can't invite you for dinner " + guest)
guest = people_dinner.pop(2)
print("sorry that i can't invite you for dinner " + guest)

#inviting the other two people 
guest = people_dinner[0]
print("you are still invited for the dinner " + guest)

guest = people_dinner[1]
print("you are still invited for the dinner " + guest)

del people_dinner[0]
print(people_dinner)
del people_dinner[0]
print(people_dinner)

len(people_dinner)
