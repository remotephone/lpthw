print "You enter a dark room with two doors. Do you go through door #1 or \
 door #2? Or 3?"

door = raw_input("> ")

if door == "1":
    print "There's a giant bear here eating a cheese cake. What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."

    bear = raw_input("> ")

    if bear == "1":
        print "The bear eats your face off. Good job!"
    elif bear == "2":
        print "The bear eats your legs off. Good job!"
    else:
        print "Well, doing %s is probably better. Bear runs away." % bear

elif door == "2":
    print "You stare into the endless abyss at Cthulhu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolvers yelling melodies."

    insanity = raw_input("> ")

    if insanity == "1" or instanity =="2":
        print "Your body survives powered by the mind of a jello. Good job!"

    else:
        print "The insanity rots your eyes into a pool of muck. Good job!"

elif door == "3":
    print "This is not a door. This is a pit. It never ends."
    print "You're falling but there's a stick. Do you grab it?"

    grab = raw_input("> ")

    if grab == "yes":
        print "You grabbed the branch! You're hanging on for dear life."
        print "But you're not fat right? Are you? Yes or no?"

        fat = raw_input("> ")

        if fat == "yes":
            print "There's nothing wrong with that, you're a beautiful person.\
But the branch breaks and you die."
        elif fat == "no":
            print "The branch doesn't break and you hang on till you starve."
        else:
            "Your lack of honesty weighs on you heavily and the branch breaks.\
You die."

    elif grab == "no":
        print "You didn't grab the branch. You fall to your doom."
    else:
        print "Still pondering your choice, you fall to your doom."


else:
    print "You stumble around and fall on a knife and die. Good job!"
