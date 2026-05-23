"""User superclass"""

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