# Числа от 1 до 20
numbers1 = []
for value in range(1,21):
	numbers1.append(value)

print(numbers1)

numbers2 = []
for value in range(1,1000001):
	numbers2.append(value)
#
#for value in range(0,1000000):
#	print(numbers2[value])
print(min(numbers2))
print(max(numbers2))
print(sum(numbers2))

numbers3 = list(range(1,20,2))

for value in numbers3:
	print(value)

numbers4 = list(range(3,31,3))

for value in numbers4:
	print(value)


cubes = []

for value in range(1,11):
	cubes.append(value**3)

for value in cubes:
	print(value)
print(cubes)

cubes2 = [value**3 for value in range(1,11)]
print(cubes2)

# parts of lists:
my_foods = ['pizza', 'falafel', 'carrot cake', 'banana','juce','pudduing','meat']
my_foods.append('cannoli')
print("My favorite foods are:")
print(my_foods)


print("The first three items in the list are:")
print(my_foods[:3])

print("Three items from the middle of the list are:")
print(my_foods[len(my_foods)//2-1:len(my_foods)//2+2])

print("Three items from the bottom list are:")
print(my_foods[-3:])


#list copy

my_foods = ['pizza', 'falafel', 'carrot cake', 'banana','juce','pudduing','meat']
nyash_foods = my_foods[:]
my_foods.append('cannoli')
nyash_foods.append('pesto')
print("My favorite foods are:")
for i in my_foods:
	print(i)

print("\nNyash favorite foods are:")
for i in nyash_foods:
	print(i)

#tuples
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

menu = ('apple','banana','meat','orange','grapes')
for i in menu:
	print(i)

#menu[1] = 'pomegranate'

menu = ('apple','onion','meat','butter','grapes')
for i in menu:
    print(i)
