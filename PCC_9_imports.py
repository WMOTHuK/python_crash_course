"""Import testing"""
from PCC_9_restoraunt import Restoraunt
import PCC_9_users

# 9-10 Import Restoraunt

monkeyndonkey = Restoraunt('Monkey and Donkey','African')
Restoraunt.open_restoraunt(monkeyndonkey)


# 9-11 Import Admin Classes

admin = PCC_9_users.Admin('Konstantin', 'Alimov', 41, 'shared@gmail.com','Male')
admin.add_priviliges(['add new users', 'block users', 'delete users'])
admin.list_priviliges()
