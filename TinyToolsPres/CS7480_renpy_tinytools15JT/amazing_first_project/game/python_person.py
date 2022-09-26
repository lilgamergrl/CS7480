import random
import names


def choose_key()
    hate_lst = ['puppies', 'kittens', 'mice', 'bears']
    hate_key = random.choice(hate_lst)
    return hate_key

def personality(hate_key):
        personality_toward_player = {'puppies':'mean','kittens':'evil','mice':'neutral','bears':'hatred'}
        return personality_toward_player[hate_key]

def backgrounds(hate_key):
    hate_dict = {'puppies':f' People knew the cave dweller {cave_dweller} was evil \n because puppies are cute!',
    'kittens':f' Everyone loved kittens so they knew to stay clear of evil cave dweller {cave_dweller}',
    'mice':' No one really minded this hate. But no one liked it either so they avoided the cave dweller.',
    'bears':'Everyone laughed at the evil cave dweller! Everyone knew bears could easily be defeated by running uphill!'}
    return hate_dict[hate_key]

def get_firstname():
    return names.get_firstname()