#for
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
    print(magician+'!!!')
print(magician+'@@@')    
#range
for value in range(1,6):
    print(value)
numbers = list(range(1,11))
print(numbers)
even_numbers = list(range(2,11,2))
print(even_numbers)
#square
squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)
squares.clear()
for value in range(1,11):
    squares.append(value**3)
print(squares)
#min, max, sum
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))
#generate list
squares = [value**4 for value in range(1,11)]
print(squares)
#practice
odd_numbers = list(range(1,21,2))
print("odd_numbers: "+str(odd_numbers))
third_numbers = list(range(3,31,3))
for third in third_numbers:
    print("third: " + str(third))
#slices - срезы
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players)
print(players[0:3])
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players)
print(players[-3:])
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
#slices: = vs []
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods1 = my_foods
friend_foods1.append('test1')
print(my_foods)
friend_foods2 = my_foods[:]
friend_foods2.append('test2')
print(my_foods)
#tuples - кортежи
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
dimensions = (300, 10)
print(dimensions[0])
print(dimensions[1])
dimensions = (300, 10, 0)
print(dimensions[0])
print(dimensions[1])
print(dimensions[2])
#if
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")
age_0 = 22
age_1 = 18
if (age_0 >= 21) and (age_1 >= 21):
    print("TEST1!")
else:
    print("TEST2!")

requested_toppings = ['mushrooms', 'onions', 'pineapple']
if 'mushrooms' in requested_toppings:
    print('mushrooms');
elif 'pepperoni' in requested_toppings:
    print('pepperoni');
else:
    print('none');

requested_toppings = ['mushrooms', 'onions', 'pineapple']
if 'qwee' not in requested_toppings:
    print('none');

can_edit = False
#if for
requested_toppings = []
for requested_topping in requested_toppings:
    print("Adding " + requested_topping + ".")
print("\nFinished making your pizza!")

if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")
print("\nFinished making your pizza!")
