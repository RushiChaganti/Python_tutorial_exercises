a = 2000
b = 200906
if a > b :
    print("a is greater than b ")

elif b > a :
    print("b is greater than a ")

else:
    print("b is equal to a ")

# doing an short hand if statement

if a > b : print("a is greater than b ")

# doing an short hand if else statement

print("a is greater than b ") if a > b  else print("b is greater than a ")

c = 20000

# trying the 'and' logical operator

if b > c and c > a:
    print(" both statements are true ")

#trying the 'or' logical opertaor 

if b < a or c > a:
    print(" one statement is true ")

# trying nested if statements

if a < b :
    print("a is less than b ")
    if b > a :
        print("b is greater than a ")









