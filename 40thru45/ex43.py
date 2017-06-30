from sys import exit
from random import randint


class Scene(object):

    def enter(self):
        print "This scene isn't ready yet"
        exit(1)


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()


class Death(Scene):

    quips = [
            "You died. lame",
            "You dead son",
            "You won! jk you died",
            "good job. losing"
    ]

    def enter(self):
        print Death.quips[randint(0, len(self.quips)-1)]
        exit(1)


class CentralCorridor(Scene):

    def enter(self):
        print "You enter the corridor. Everythings dead and lame but here you "
        print "are all dumb. You need to get to the armory, get a bomb, put in the"
        print "bridge and blow the ship up. If you want to survive you need to "
        print "get into an escpate pod too. On the way there you run into a "
        print "Gothon, a scary alien! What do you do!? he has a gun! Are you "
        print "going to shoot, dodge, or distract him by telling a joke?"

        action = raw_input("> ")

        if "shoot" in action:
            print "Quick on the draw you pull your blaster and fire at the "
            print "alien. How costume is flowing which throws off your aim, "
            print "you miss, but he doesn't. With his mouth. He eats you."
            return 'death'

        elif "dodge" in action:
            print "Like a world class boxer, you dodge, and the blaster blazes"
            print " past your head."
            return 'death'

        elif "joke" in action:
            print "Thinking quick, you tell him the only Gorthon joke you "
            print "know. \"What's the difference between a Gothon and a "
            print "chickpea?\" I never had a Gothon my face.\" The Gothon "
            print "freezes in his tracks, shudders, and then laughs a hearty "
            print "laugh. You shoot him in the face. The way is clear."
            return 'laser_weapon_armory'
        else:
            print "DOES NOT COMPUTE"
            return 'central_corridor'


class LaserWeaponArmory(Scene):

    def enter(self):
        print "You enter the armory and its quiet. You run to the other side "
        print "of the room and find a keypad lock on a box. You need to code "
        print "to get the bomb out. If yu get the code wrong 10 times the "
        print "lock closes and you won't get the bomb. It's a 3 digit code."
        code = "%d%d%d" % (randint(1, 9), randint(1, 9), randint(1, 9))
        guess = raw_input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:
            print "BZZZZZEDD!"
            guesses += 1
            guess = raw_input("[keypad]> ")

        if guess == code:
            print "The container opens -poof!- and you grab the bomb. You run "
            print "to the bridge as quick as you can!"
            return 'the_bridge'
        else:
            print "The lock buzzes one last time and you hear it lock for "
            print "good. You sit there and wait for your doom. You die."
            return 'death'


class TheBridge(Scene):

    def enter(self):
        print "You enter the bridge with your bomb and surprise 5 Gothons "
        print "trying to take over the ship. Each of them has their weapon "
        print "out and sees the bomb, but don't want to set it off."

        action = raw_input("> ")

        if action == "throw the bomb":
            print "In a panic you throw the bomb and leap at the door. Right "
            print "as you drop it a Gothon shoots you in the back and kills "
            print "you. As you die, you see them disarm the bomb."
            return 'death'

        elif action == "slowly place the bomb":
            print "You point the blaster at the bomb under your arm and the "
            print "aliens sweat. You inch backwards to the door, open it, "
            print "and carefully place the bomb. You close the door, keeping "
            print "the Gothons from disarming it. As they freak, you dash to "
            print "the escape pod."
            return 'escape_pod'
        else:
            print "DOES NOT COMPUTE"
            return 'the_bridge'


class EscapePod(Scene):

    def enter(self):
        print "You rush through the ship to the pod. You need to pick one of "
        print "five pods. Which one do you take?"
        good_pod = randint(1, 5)
        guess = raw_input("[pod #]> ")

        if int(guess) != good_pod:
            print "?You jump into pod %s and hit eject." % guess
            print "The pod pops into space and implodes. You chose the wrong "
            print "one sucker."
            return 'death'
        else:
            print "You jump into pod %s and hit eject" % guess
            print "The pod slides into space, as it flies, you see the ship "
            print "implode behind you, taking the Gothons with it. You win!"
            return 'finished'


class Finished(Scene):

    def enter(self):
        print "You won! Good job!"
        return 'finished'


class Map(object):

    scenes = {
            'central_corridor': CentralCorridor(),
            'laser_weapon_armory': LaserWeaponArmory(),
            'the_bridge': TheBridge(),
            'escape_pod': EscapePod(),
            'death': Death(),
            'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
