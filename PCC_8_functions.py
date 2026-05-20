

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
def default_shirt(size = "L", text = "I love python"):
    """generates default L T-shirt"""
    print(f"Here is your shirt with {size} size and text '{text}'")
default_shirt()
default_shirt("XXL", "I'm HUGE")

# 8-5 cities
def describe_city(city, country = "Russia"):
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

while True:
    print("let's create an album")
    print("(enter 'q' at any time to quit)")
    artist = input("Please enter Artist: ")
    if artist == "q":
        break
    name = input("Please ender Album name: ")
    if name == "q":
        break
    print(make_album(artist, name))
