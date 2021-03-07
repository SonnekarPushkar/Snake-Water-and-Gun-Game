#  SNAKE , WATER AND GUN GAME : PROJECT 1

import random

# function defined:

def gamewin(comp,b):
    if comp == b:
        return None
    if comp == 's':
        if b == 'w':
            return False
        elif b == 'g':
            return True
    elif comp == 'w':
        if b == 's':
            return True
        elif b == 'g':
            return False
    elif comp == 'g':
        if b == 's':
            return False
        elif b == 'w':
            return True

#Computers random response :

randno = random.randint(1,3)
print("Comp Turn : Snake(s) , Water(w) , Gun(g) : ")

# If statements response on the number chosen randomly by the computer:

if randno == 1:
    comp = 's'
elif randno == 2:
    comp = 'w'
elif randno == 3:
    comp = 'g'

# Users input :

b = input(" Your turn : Snake(s) , water(w) or gun(g) ? ")

a = gamewin(comp,b)

print(f"You chose : {b}")
print(f"Computer chose : {comp}")

if a == None:
    print("The game is tied.")
elif a == True:
    print("You win !")
else:
    print("You lose .")