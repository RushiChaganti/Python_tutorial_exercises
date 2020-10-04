"""
favorite_fruits = ['apple', 'orange', 'pineapple']
if 'bananas' in favorite_fruits:
    print("You really like bananas!")
if 'apple' in favorite_fruits:
    print("You really like apple!")
if 'guava' in favorite_fruits:
    print("You really like guava!")
if 'kiwis' in favorite_fruits:
    print("You really like kiwis!")
if 'custard apple' in favorite_fruits:
    print("You really like custard apple!")
"""
    
def favorite_fruits(fruit):
    favorite_fruits = ['apple', 'orange', 'pineapple']
    if fruit in favorite_fruits:
        print(f"You really like {fruit}!")


favorite_fruits("apple")    
favorite_fruits("orange")    
favorite_fruits("pineapple")
favorite_fruits("bananas")
