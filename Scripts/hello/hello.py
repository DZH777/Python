print("Hello, Igor!")
# variables
message = "Hello Python world!"
print(message)
message = "Hello Python world!!!"
print(message)
# rows
name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())
#concatenate
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " +++ " + last_name
print(full_name)
print("Hello, " + full_name.title() + "!")
#tab and new row
print("\t"+full_name)
print("\tText")
print("Text1\nText2")
#trim
print(" 1111 ".rstrip())
print(" 1111 ".lstrip())
#apostrophe
message = "One of Python's strengths is its diverse community."
print(message)
message = 'One of Python''s strengths is its diverse community.'
print(message)
#numbers
num = 0.2 + 0.2
print(num)
num1 = 0.2 + 0.1
print(num1)
age = 23
message = "Happy " + str(age) + "rd Birthday!"
print(message)
print(3 / 2)
#lists
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[1].title())
print(bicycles[-1])
print(bicycles[-2])
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)
motorcycles.append('lada')
print(motorcycles)
lists = []
lists.append('root')
print(lists)
lists.insert(0, 'leaf')
print(lists)
del lists[1]
print(lists)
popped_lists = lists.pop()
print(lists)
print(popped_lists)
lists.append('root1')
lists.append('root2')
lists.append('root3')
popped_lists = lists.pop(1)
print(lists)
print(popped_lists)
lists.append('root3')
lists.append('root3')
lists.remove('root3')
print(lists)
lists.remove('root3')
print(lists)
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars,reverse=True))
print("\nHere is the original list again:")
print(cars)
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)
print(len(cars))













