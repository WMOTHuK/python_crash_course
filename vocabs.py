nyasha = {
        'name':'Nastya',
        'lname':'Malysheva',
        'age': 33,
        'city':'Vladimir'
}
for key, value in nyasha.items():
    print(f"{key.title()} - {value}")

numbers = {
        'Kosta':[27,2],
        'Nyasha':[18,3],
        'Vladimir': [13,3],
        'Yarik':[13,12],
        'Varvar':[21,9]
}
for key, value in numbers.items():
    print(f"\n{key.title()}'s favorite numbers:")
    for i in value:
        print(f"{i} is his favorite number!")

glossary = {
        'Kosta': "Alimov",
        'Nyasha':"Malysheva",
        'Vladimir': "Putin",
        'Yarik': "Alimov",
        'Varvar':"Alimova"
}
for key, value in glossary.items():
    print(f"\n{key.title()}'s surname - {value}")

rivers = {
        'nile':"egypt",
        'volga':"russia",
        'Amazon':"Brazil"
}
for key, value in rivers.items():
    print(f"\n{key.title()} runs through {value.title()}.")
for key in rivers.keys():
    print(f"\n{key.title()} is a river")
for value in rivers.values():
    print(f"\n{value.title()} is a country")


favorite_languages = {
                    'jen': 'python',
                    'sarah': 'c',
                    'edward': 'ruby',
                    'phil': 'python',
                    }
people = ['pete','jen', 'edward','phil', 'Yarik','nyasha','kosta']

for person in people:
    if person in favorite_languages.keys():
        print(f"\n{person.title()}, thanks for the poll!")
    else:
        print(f"\n{person.title()}, can you do a poll, please?")

nyasha = {
        'name':'Nastya',
        'lname':'Malysheva',
        'age': 33,
        'city':'Vladimir'
         }
kosta = {
        'name':'Kostya',
        'lname':'alimov',
        'age': 41,
        'city':'Vladimir'
         }
yarik = {
        'name':'Yaroslav',
        'lname':'Alimov',
        'age': 7,
        'city':'Vladimir'
         }

people = [nyasha, kosta, yarik]

for person in people:
    print(f"\nFull name: {person['name']} {person['lname']}")
    print(f"Age: {person['age']}. Lives in {person['city']}")


cities = {
        'Vladimir':{
                    'population': 300000,
                    'prices': 'average',
                    'region': 'Vladimir region'
                    },
        'Moscow':{
                    'population': 20000000,
                    'prices': 'high',
                    'region': 'Moscow region'
                    },
        'Suzdal': {
                    'population': 50000,
                    'prices': 'very high',
                    'region': 'Vladimir region'
                    },
        }

for city, props in cities.items():
    print(f"City of {city} is situated in {props['region']}.") 
    pop = props['population']
    print(f"It has population of {pop:,} people .".replace(',', ' '))
    print(f"The prices there {props['prices']}.") 