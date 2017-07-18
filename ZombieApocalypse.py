print("Doomsday")
print ("You are walking down the roadside of your town in Snellville, Georgia.")
print("You are exhuasted after a long day of work.")
print("You are thinking about all the things you have left to do when you are pulled from your thoughts by a disturbing sound.")
print("Characters: Business Woman or Artist.")


def stahp():


    choose = input("Which character would you like?: ")
    if choose == "Business Woman":
        print("You decide that you are just being silly and continue on your path.")
        print("As you continue down the road, the sound continues to grow louder.")
    elif choose == "Artist":
        print("You begin to slightly panic, but decide it would be best to just continue.")
        print("As you continue down the road, the sound continues to grow louder.")
    else:
        print("Bruh, choose one that is provided...")
        stahp()

stahp()

def one ():
    choice_one = input("Do you want to run home or hide out?: ")
    def run():
            print("You safely make it to your home and unlock the front door.")
            print("As you make your way to the bedroom, you hear that disturbing noise once more.")
            print("You open your bedroom door and a zombie pushes through and eats ya brain. Get wrecked...")
            exit()
    if choice_one == "run home":
        run()
    elif choice_one == "hide out":
        print("You quickly make your way to the farm up ahead.")
        print("As you arrive, you realize that the noise is getting louder from the road behind you.")
        print("When you approach the door, you notice movement through the window.")
    else:
        print("Bruh, choose one that is provided...")
        one()
one()

def two():
    choice_two = input("Do you go in or run home?")

    if choice_two == "run home":
        run()
    elif choice_two == "go in":
        print("As you enter the farmhouse, you hear loud groaning upstairs.")
    else:
        print("Bruh, choose one that is provided...")
        two()
two()

def three():
    choice_three = input ("Do you go upstairs or investigate downstairs?")

    if choice_three == "go upstairs":
        print("You carefully make your way upstairs only to find a herd of zombies.")
        print("The zombies eat ya brains. Get wrecked...")
        exit()
    elif choice_three == "investigate downstairs":
        print("You investigate your surroundings in hopes to find a weapon. You stumble upon two items that may be of use.")
        print("Which one would you like to pick up?")
    else:
        print("Bruh, choose one that is provided...")
        three()
three()

def four():
    choice_four = input("Would you like to pick up the hammer or the spoon?")

    if choice_four == "pick up the hammer":
        print("You pick up the hammer and make your way up the stairs.")
        print("You locate the source of the noise. You smash the zombies' brains out and survive!!!")
        print("You later discover that your whole town was brutally murdered, but since you were smart")
        print("unlike the others, you get to live a sad lonely life in the farmhouse.")
    elif choice_four == "pick up the spoon":
        print ("You pick up the spoon and make your way up the stairs.")
        print("You spot the herd of zombies and you throw your spoon at them!")
        print("They look at you, dumbfounded by your stupidity and eat ya brains. Get wrecked...")
    else:
        print("Bruh, choose one that is provided...")
        four()
four()
