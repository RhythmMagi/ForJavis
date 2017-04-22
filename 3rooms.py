from sys import exit

class Scene(object):

    def enter(self):
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()

        while current_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()

class RedRoom(Scene):

    def enter(self):
        print "You have entered the Red Room"
        print "What room would you like to enter?: Green or Blue?"

        action = raw_input("> ")

        if action == "Green":
            return 'GreenRoom'

        elif action == "Blue":
            return 'BlueRoom'

        else:
            print "Please enter: 'Green' or 'Blue'"
            return 'RedRoom'

class GreenRoom(Scene):

    def enter(self):
        print "You have entered the Green Room"
        print "What room would you like to enter?: Red or Blue?"

        action = raw_input("> ")

        if action == "Red":
            return 'RedRoom'

        elif action == "Blue":
            return 'BlueRoom'

        else:
            print "Please enter: 'Red' or 'Blue'"
            return 'GreenRoom'

class BlueRoom(Scene):

    def enter(self):
        print "You have entered the Blue Room"
        print "What room would you like to enter?: Red or Green?"

        action = raw_input("> ")

        if action == "Red":
            return 'RedRoom'

        elif action == "Green":
            return 'GreenRoom'

        else:
            print "Please enter: 'Red' or 'Green'"
            return 'BlueRoom'

class Map(object):

    scenes =  {
    'RedRoom': RedRoom(),
    'GreenRoom': GreenRoom(),
    'BlueRoom': BlueRoom(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('RedRoom')
a_game = Engine(a_map)
a_game.play()
