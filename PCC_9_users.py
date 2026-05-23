"""User-specific classes"""

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