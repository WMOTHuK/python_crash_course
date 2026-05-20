car = 'Subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

print("Is car == 'subaru'? I predict True.")
print(car.lower() == 'subaru')

num = 832

print(num == 100)
print(num > 100)
print(num < 100)
print(num >= 832)
print(num <= 100)

print(num > 100 and car.lower() == 'subaru')
print(num < 100 and car.lower() == 'subaru')
print(num < 100 or car.lower() == 'subaru')

digits = ['1','2','3','4','5']

print('8' in digits)
print('1' in digits)

print('8' not in digits)
print('1' not in digits)


age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

alien_color = 'green'

if alien_color == 'green':
    print("You scored 5 points")
 

alien_color = 'red'
# if-else
if alien_color == 'green':
    print("You scored 5 points")
else:
    print("You scored 10 points")

    
# if-elif
alien_color = 'black'
points = 0
if alien_color == 'green':
    points = 5
elif alien_color == 'yellow':
    points = 10
elif alien_color == 'red':
    points = 15

print("\nYou scored " 
    + str(points) 
    + " points! \nEnemy color was " 
    + alien_color
    + " !" )

age = 40
name = ''
if age < 2:
    name = 'justborn' 
elif age>=2 and age<4:
    name = 'baby'
elif age>=4 and age<13:
    name = 'kid'
elif age>=13 and age<20:
    name = 'youngling'
elif age>=20 and age<65:
    name = 'grownup'
elif age > 65:
    name = 'oldone'
print("\n Your age is " + str(age) + "years!"
    + "\n You are a " + name + "!")


favorite_fruits = ['apple', 'orange', 'pomegranate']


all_fruits = ['banana','onion','grapes','melon','apple']
for i in all_fruits:    
    if i in favorite_fruits:
        print("\nYou really like " + i + "!")
    else:
        print("\nYou don't like " + i + "!")

users = [
        'Nick','Sam','Dick','Kosta',
        'Gareth','Yarik', 'Nastya',
        'Varvar','admin'
        ]

new_users = [
        'Vova','Misha','Kolya',
        'gareth','yarik', 'NAstya',
        'Olga', 'Sergey'
        ]

if users :
    for i in users:
        if i == 'admin' :
            print("\nHello " + i + "!"
                + "\n Would you like to see a status report?")
        else :
            print("\nHello " + i + "!"
                + "\nThank you for logging in again")
else:
    print("No users exists.")      

for value in new_users :
    if value.lower() in [user.lower() for user in users]:
        print("\nName " + value + " is busy!"
            + "\nPick another name.")
    else:
        print("\nName " + value + " is available!")

nums = list(range(1,10))
print(nums)

for i in nums:
    if i == 1:
        suff = 'st'
    elif i == 2:
        suff = 'nd'
    elif i == 3:
        suff = 'rd'
    else: 
        suff = 'th'
    print(str(i)+suff)
