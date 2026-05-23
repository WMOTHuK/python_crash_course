from PCC_9_usersubs import(Admin)

# 9-12 Multimodules

admin = Admin('Konstantin', 'Alimov', 41, 'shared@gmail.com','Male')
admin.add_priviliges(['add new users', 'block users', 'delete users'])
admin.list_priviliges()
