""" User subclasses"""
from PCC_9_onlyusers import User
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