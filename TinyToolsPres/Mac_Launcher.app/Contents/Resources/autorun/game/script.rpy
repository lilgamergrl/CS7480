init python:
    import random

    def choose_key():
        hate_lst = ['puppies', 'kittens', 'mice', 'bears']
        hate_key = random.choice(hate_lst)
        return hate_key

    def personality_towards(hate_key):
        personality_toward_player = {'puppies':'mean','kittens':'evil','mice':'neutral','bears':'hatred'}
        return personality_toward_player[hate_key]

    def backgrounds(hate_key):
        hate_dict = {'puppies':f' People knew the cave dweller {c} was evil \n because puppies are cute!',
        'kittens':f' Everyone loved kittens so they knew to stay clear of evil cave dweller {c}',
        'mice':' No one really minded this hate. But no one liked it either so they avoided the cave dweller.',
        'bears':'Everyone laughed at the evil cave dweller! Everyone knew bears could easily be defeated by running uphill!'}
        return hate_dict[hate_key]

    def get_first_name():
        f = open("/Users/jess/Desktop/CS7480_renpy_tinytools15JT/amazing_first_project/game/names/names.txt", "r")
        data = f.read()
        data = data.split('\n')
        return random.choice(data)
    def get_evil_occupation():
        f = open("/Users/jess/Desktop/CS7480_renpy_tinytools15JT/amazing_first_project/game/names/occs.txt", "r")
        data = f.read()
        data = data.split('\n')
        return random.choice(data)
    ename = get_first_name()
    bname = get_first_name()
    cname = get_first_name()
    aname = get_first_name()
# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
#image bestiepng = im.Scale("ichikocasualsmile.png", 700, 950)
#image smilepng = im.Scale("ichikocasualsmile.png", 700, 950)

define a = Character(aname, image = "ichikocasualsmile.png")
define e = Character(ename)
define b = Character(bname)
define c = Character(cname)

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    
    # Allows you to use python syntax and code inside of the game
    init python:
        '''
        The four statements that work with images are:

        image - defines a new image.
        show - shows an image on a layer.
        scene - clears a layer, and optionally shows an image on that layer.
        hide - removes an image from a layer.

        As abrupt changes of image can be disconcerting to the user, Ren'Py has the with statement, which allows effects to be applied when the scene is changed.
        https://www.renpy.org/doc/html/displaying_images.html
        '''
        # Variables to make the story random
        hate_key = choose_key()
        background_var = backgrounds(hate_key)
        personality_tow = personality_towards(hate_key)
        occupation = get_evil_occupation()
    
    scene beach
    image smile = im.Scale("ichikocasualsmile.png", 700, 950)
    show smile

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    e "There once was a story about an evil cave dweller name [cname]!"
    
    e "They were the most evil [occupation] in the world!"

    e "The evil cave dweller hated [hate_key]!"
    #show Cave
    # ^ Clicking show cave will just show the background
    # Below we will use scene cave to clear the image layers and start fresh

    scene cave
    # These display lines of dialogue.
    # g "Welcome to the Nekomimi Institute, [playername]!"
    image player2 = im.Scale("py2.png", 700, 950)
    show player2
    b "[background_var]"
    b " -- but the Evil [cname] never listened."

    init python:
        def random_img_file():
            lst = ['villageshop.png', 'villagetavern3.png', 'snow1.png']
            return random.choice(lst)
        val = random_img_file()
        val2 = random_img_file()
    scene val
    image frown = im.Scale("ifrown.png", 700, 950)
    show frown
    b "Random characters can talk here if you want them to."
    # This ends the game.

    scene val2
    a "This is the end of the game."
    return
