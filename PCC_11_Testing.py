""" Python Crash Course Chapter 11 - Testing"""

#11-1 and 11-2 Towns and Countries

def get_town_desc(city, country, population=''):
    if population:
        return((city + ", " + country).title() + 
            " - population " + str(population))
    else:
        return((city + ", " + country).title())
    

#11-3 Employee
class Employee():
    """Describes an employee"""
    def __init__(self, name, surname, salary):
        """Constructor"""
        self.first_name = name
        self.last_name = surname
        self.salary = salary
    
    def give_raise(self, increase=5000):
        """Increase salary by certain amount (default - 5000)"""
        self.salary += increase