


# 8-1 Message

def display_message():
    """Just a message printout"""
    print("Python uses functions all the time")

display_message()

# 8-2 #Favorite book
def favorite_book(title):
    """prints out favorite book"""
    print(f"One of my favorite books is {title}")

favorite_book("M A N I A C")

# 8-3 T-shirt
def make_shirt(size, text):
    """generates T-shirt"""
    print(f"Here is your shirt with {size} size and text '{text}'")
make_shirt("S","i'm small")
make_shirt(size = "L", text = "I'm large")

# 8-3 Big shirts
def default_shirt(size="L", text="I love python"):
    """generates default L T-shirt"""
    print(f"Here is your shirt with {size} size and text '{text}'")
default_shirt()
default_shirt("XXL", "I'm HUGE")

# 8-5 cities
def describe_city(city, country="Russia"):
    """Describes a city by country"""
    print(f"{city} is situated in {country}")
describe_city('Vladimir')
describe_city('Moscow')
describe_city('Beijing', "China")

# 8-6 city names

def city_country(city, country):
    """Returns a city-country string"""
    description = city + ', ' + country
    return description


""" while True:
    print("let's describe a city")
    print("(enter 'q' at any time to quit)")
    city = input("Please enter city: ")
    if city == "q":
        break
    country = input("Please ender country: ")
    if country == "q":
        break
    print(city_country(city, country))
 """

# 8-7 Album
def make_album(artist, album, songs =''):
    """Generates a music album"""
    album_vocab = {'artist' : artist, 'Album' : album }
    if songs:
        album_vocab['songs']  = songs
    return album_vocab


album_data = [
                {'artist': 'Motorhead', 'album' : 'Head of motors'},
                {'artist': 'Metallica', 'album' : 'Reload'},
                {'artist': 'Guano apes', 'album' : 'Ape Jazz', 'songs': 13}
            ]

for item in album_data:
    print(make_album(**item))



# 8-8 user albums
""" while True:
    print("let's create an album")
    print("(enter 'q' at any time to quit)")
    artist = input("Please enter Artist: ")
    if artist == "q":
        break
    name = input("Please ender Album name: ")
    if name == "q":
        break
    print(make_album(artist, name))
 """

# 8-9 magicians
magicians = ['David Copperfield', 'Benny Kravits', 'Frank Copolla']

def list_magicians(magicians):
    """Displays all magicians in the list"""
    print("There are these magicians in the list:")
    for mage in magicians:
        print(mage)

list_magicians(magicians)

# 8-10 Great magicians
def make_great(magicians):
    """ Adds prefix 'The Great' to everything in the list"""
    for num in range(len(magicians)):
        magicians[num] = "The Great " + str(magicians[num])



make_great(magicians)
list_magicians(magicians)

# 8-11 Forbid changes
magicians = ['David Copperfield', 'Benny Kravits', 'Frank Copolla']
def make_great_ret(magicians):
    """ Adds prefix 'The Great' to everything in the list"""
    for num in range(len(magicians)):
        magicians[num] = "The Great " + str(magicians[num])
    return magicians
great_mages = make_great_ret(magicians[:])

list_magicians(magicians)
list_magicians(great_mages)

# 8-12 Sandwiches
def make_sandwich(*ingridients):
    """Prints out a sandwich preparation"""
    print("Starting to make your sandwich")
    sostav = ''
    for food in ingridients:
        sostav = sostav + '\n  ' + food.title()
    print(f"Your sandwich is ready. Here is what it consists of: {sostav}")

make_sandwich('Bread', 'Salad', 'Meat')
make_sandwich('Bread', 'Salad', 'Meat', 'Tomato')
make_sandwich('Bread', 'Salad', 'Fish', 'Tomato')

# 8-13 Profile

def build_profile(first, last, **user_info):
    """Строит словарь с информацией о пользователе."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_profile('Konstantin', 'Alimov',
                            age=43,
                            proffesion='Analyst',
                            family_status='Married')
print(user_profile)

# 8-14 Cars

def make_car(brand, model, **specs):
    """Builds a vocab about a car."""
    car = {}
    car['Brand'] = brand
    car['model'] = model
    for key, value in specs.items():
        car[key] = value
    return car

car = make_car(
                'Nissan', 'X-trail',
                colour='black',
                engine='2,5L',
                year=2019,
                name='Candy'               
                )

print(car)

# 8-15 Print models (module import)
#Simple import
""" 
import printing_functions

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
printing_functions.print_models(unprinted_designs, completed_models)
printing_functions.show_completed_models(completed_models) """

# 8-16 Оther imports
# Function + Function alias
""" 
from printing_functions import print_models as pm
from printing_functions import show_completed_models

unprinted_designs = ['Order 4', 'Order 5', 'Order 6']
completed_models = []
pm(unprinted_designs, completed_models)
show_completed_models(completed_models) """

#Import all functions

""" from printing_functions import *

unprinted_designs = ['Order 7', 'Order 8', 'Order 9']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models) """

#Import module as alias 

""" import printing_functions as pf

unprinted_designs = ['Order 10', 'Order 11', 'Order 12']
completed_models = []
pf.print_models(unprinted_designs, completed_models)
pf.show_completed_models(completed_models) """