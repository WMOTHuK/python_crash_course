
# prompt = "\nPlease add some toppings if you want.(4 max)"
# prompt += "\n(Enter 'quit' when you are finished.) "

# i = 0.
# while i < 4:
#     topping = input(prompt)
#     if topping == 'quit':
#         break
#     if topping == 'fuck you':
#         i = 6
#     else:
#         print(f"{topping} was added to your pizza.")


# prompt = "please enter your age to define ticket price"

# age = int(input(prompt))

# if age < 3:
#     price = 0 
# elif age >= 3 and age < 13:
#     price = 10
# elif age > 12 :
#     price = 20

# print(f"The price of ticket for you is {price} dollars.")




# sandwich_orders = ['pastrami', '2nd','pastrami','4th','pastrami']
# finished_sandwiches = []

# print(f"Sorry, we ran out of pastrami.")
# while 'pastrami' in sandwich_orders:
#     sandwich_orders.remove('pastrami')


# while sandwich_orders:
#     ready_sandwich = sandwich_orders.pop()
#     print(f"I made your {ready_sandwich} sandwich!")
#     finished_sandwiches.append(ready_sandwich)
# print(f"Here is a list of ready sandwiches")
# for i in finished_sandwiches:
#     print(f"{i} sandwich")

travels = {}
pname = "What's your name?"
pplace = "Where yuo want to travel?"
pquest = "You are the last one to poll?"
active = True
while active:
    name = input(pname)
    place = input(pplace)
    travels[name] = place
    answer = input(pquest)
    if answer == 'yes':
        active = False

print("\nHere are the poll results:")


for name, place in travels.items():
     print(f"{name} wants to travel to {place}.")