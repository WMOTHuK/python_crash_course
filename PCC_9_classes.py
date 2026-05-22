# 9-1 Restoraunt

class Restoraunt():
    """Simple restoraunt model"""
    def __init__(self, name, cuisine):
        """Constructor"""
        self.restaurant_name = name
        self.cuisine_type = cuisine
        self.number_served = 0

    def describe_restoraunt(self):
        """Prints out resoraunt info"""
        print(f"\nYour restoraunt '{self.restaurant_name}'.")
        print(f"Your restoraunt serves a {self.cuisine_type} cuisine.")       

    def open_restoraunt(self):
        """Prints out an opening message"""
        print("Opening restoraunt .....")
        print(f"Your restoraunt {self.restaurant_name} is now open.")
    
    def dishes_served(self):
        """Outputs number od served dishes"""
        message = ("Restoraunt " + self.restaurant_name 
           + " has served " + str(self.number_served) + " dishes.")
        print(message)

    def set_numbers_served(self, dishes_served):
        """Sets number of served dishes"""
        self.number_served = dishes_served

    def increment_number_served(self, incriment):
        """Incriments dishes served by 'incriment' value"""
        self.number_served += incriment


dognfog = Restoraunt("Dog and Fog", 'Russian')
print(dognfog.restaurant_name)
print(dognfog.cuisine_type)
dognfog.describe_restoraunt()
dognfog.open_restoraunt()


# 9-2 Three restoraunts

dogndog = Restoraunt("Dog and Dog", 'Korean')
porknfork = Restoraunt("Pork and Fork", "Muslim")
meatnwheat = Restoraunt("Meat and Wheat", "Pumpling")

dogndog.describe_restoraunt()
porknfork.describe_restoraunt()
meatnwheat.describe_restoraunt()


# 9-3 Users
class User():
    """Holds user info"""
    def __init__(self, first_name, last_name, age, email, sex ):
        """Constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.sex = sex
        self.login_attempts = 0

    def describe_user(self):
        """Prints out user info"""
        description = ("Current user is " 
        + self.first_name + " " + self.last_name + "."
        + "\n User is " + self.sex + " of " + str(self.age) +" years"
        + "\n Email to: " + self.email)
        print(description)
                      
    def greet_user(self):
        """Greets a user on logon"""
        print(f" Hello, {self.first_name} {self.last_name}!")
        print(" Nice to see you again.\n")

    def increment_login_attempts(self):
        """Incriments login attempts"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Resets login attempts"""
        self.login_attempts = 0
    
    def print_current_login_attempts(self):
        """ prints current login attempts value"""
        print(f'Your already done {self.login_attempts} login attempts.')


nyash = User('Anastasiya', 'Malysheva', 33, 'cuckoo@gmail.com','Female')
kost = User('Konstantin', 'Alimov', 41, 'shared@gmail.com','Male')
yara = User('Yaroslav', 'Alimov', 7, 'yarik@gmail.com','Kid')

nyash.describe_user()
nyash.greet_user()

kost.describe_user()
kost.greet_user()

yara.describe_user()
yara.greet_user()

# 9-4 Guests

restoraunt = Restoraunt('Pig and Donkey', 'Malasian')

restoraunt.dishes_served()

restoraunt.number_served = 10
restoraunt.dishes_served()

restoraunt.set_numbers_served(15)
restoraunt.dishes_served()

restoraunt.increment_number_served(15)
restoraunt.dishes_served()


# 9-5 Login Attempts

kost.increment_login_attempts()
kost.increment_login_attempts()
kost.increment_login_attempts()
kost.increment_login_attempts()
kost.increment_login_attempts()
kost.print_current_login_attempts()

kost.reset_login_attempts()
kost.print_current_login_attempts()

# 9-6 Icecream Kiosk

class IceCreamStand(Restoraunt):
    """ Child class for restoraunt"""
    def __init__(self, name, cuisine):
        super().__init__(name, cuisine)
        self.flavours = []

    def add_flavour(self, flavours = []):
        """Adds new flavour to flavour list"""
        for flavour in flavours:
            self.flavours.append(flavour)
    
    def list_flavours(self):
        """ Lists all flavours available"""
        print("Following flavours are available now:")
        for i in self.flavours:
            print(f' - {i.title()}')

icymelon = IceCreamStand('Icymelon', 'Icecream')
new_flavours = ['banana', 'apple', 'melon']
icymelon.add_flavour(new_flavours)
icymelon.add_flavour(['chocolate', 'coke', 'weed'])
icymelon.list_flavours()

# 9-7 Administrator
class Admin(User):
    """Admin user data"""
    def __init__(self,first_name, last_name, age, email, sex):
        super().__init__(first_name, last_name, age, email, sex)
        self.priviliges = []

    def add_priviliges(self, priviliges = []):
        """Adds new priviliges to priviliges list"""
        for item in priviliges:
            self.priviliges.append(item)
            
    def list_priviliges(self):
        """ Lists all priviliges available"""
        print("Here's a list of admin priviliges:")
        for item in self.priviliges:
            print(f' - {item.title()}')    

admin = Admin('Konstantin', 'Alimov', 41, 'shared@gmail.com','Male')
admin.add_priviliges(['add new users', 'block users', 'delete users'])
admin.list_priviliges()

# 9-8 Priviliges
class Priviliges():
    """Holds all priviliges data"""
    def __init__(self):
        self.priviliges = []

    def add_priviliges(self, priviliges = []):
        """Adds new priviliges to priviliges list"""
        for item in priviliges:
            self.priviliges.append(item)
            
    def list_priviliges(self):
        """ Lists all priviliges available"""
        print("Here's a list of admin priviliges:")
        for item in self.priviliges:
            print(f' - {item.title()}')    

class ComplexAdmin(User):
    """Complex Admin user data"""
    def __init__(self,first_name, last_name, age, email, sex):
        super().__init__(first_name, last_name, age, email, sex)
        self.priviliges = Priviliges()

complex_admin = ComplexAdmin(
                            'Konstantin',
                            'Alimov', 
                            41,
                            'shared@gmail.com',
                            'Male'
                            )
complex_admin.priviliges.add_priviliges([
                                        'add new users',
                                        'block users',
                                        'delete users',
                                        'ban users'
                                        ])
complex_admin.priviliges.list_priviliges()

# 9-9 Battery Refresh
class Car():
    """Simple Car model."""
    def __init__(self, make, model, year):
        """Constructor"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        """ Describes car"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Prints odometer values"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    def update_odometer(self, mileage):
        """Updates odometer values"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self, miles):
        """Increases odometer values"""
        self.odometer_reading += miles

class Battery():
    """Simple Car Battery model"""
    def __init__(self, battery_size=70):
        """Constructor"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Shows battery capacity"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def upgrade_battery(self):
        """Upgrades a battery to 85 kWh"""
        if self.battery_size < 85:
            self.battery_size = 85

    def get_range(self):
        """Outputs an average mileage for the battery"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)


class ElectricCar(Car):
    """E-car specific data"""
    def __init__(self, make, model, year):
        """Constructor"""
        super().__init__(make, model, year)
        self.battery = Battery()

tesla = ElectricCar('Tesla','Roadster',2019)
tesla.battery.get_range()
tesla.battery.upgrade_battery()
tesla.battery.get_range()