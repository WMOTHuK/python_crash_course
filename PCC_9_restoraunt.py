"""Restoraunt specific classes"""

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