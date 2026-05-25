""" Python Crash Course Chapter 10 (JSON)"""
#standard imports

#local imports
from PCC_input_functions import getuserint
from PCC_json_functions import (write_value_to_json,
                                read_value_from_json)

# 10-11 and 10-12 Favourite number

# Write to Json file
def ask_number():
    """Asks a user favourite number"""
    prompt = "Input your favourite number: \n"
    fav_num = getuserint(prompt)
    return fav_num


filename = 'favourite_num.json'
# Read from Json file
your_num = read_value_from_json(filename)
if your_num is not None:
    print(f'Your favourite number is {your_num} !')
else:
    fav_num = ask_number()
    write_value_to_json(filename, fav_num)


