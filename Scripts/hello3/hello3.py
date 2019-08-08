import random

#dictionary - словари
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

alien_0['x_position'] = 0
alien_0['y_position'] = 25
alien_0['x_position'] = 11
print(alien_0)

alien_1 = {}
alien_1['planet'] = 'MARS'
print(alien_1)
del alien_1['planet']
print(alien_1)

alien_2 = {
        'colors':['red', 'black', 'green'],
        'points':[0, 1, 2]
        }
print(alien_2)
print(alien_2['colors'][1] + ' - ' + str(alien_2['points'][2]))


user_0 = {'sex': 'M', 'age': 40, 'height': 182, 'weight': 97}
for key, value in user_0.items():
    print("Key: " + key.title() + " Value: " + str(value).title())
print("--KEY--")
for key in user_0.keys():
    print(key.title())
print("--KEY--")
for key in user_0:
    print(key.title())
print("--VALUE--")
for key in user_0.keys():
    print(str(user_0[key]).title())
print("--VALUE--")
for value in user_0.values():
    print(str(value).title())
#check in dictionary
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")
#sorted
print("--SORTED--")
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")
#set
print("--SET--")
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())
#dictionary and lists
print("--NESTED--")
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)
print("--ALIENS--")
aliens = []
colors = ['red', 'black', 'green']
for cnt in range(10):
    new_alien = {'color': colors[random.randint(0, 2)], 'points': cnt}
    aliens.append(new_alien)
print(aliens)
print("--LISTS IN--")
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}
for name, languages in favorite_languages.items():
    if len(languages) > 1:
        print("\n" + name.title() + "'s favorite languages are:")
        for language in languages:
            print("\t" + language.title())
    else:
        print("\n" + name.title() + "'s favorite language are:")
        print("\t" + languages[0].title())
print("--DIC IN DIC--")
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}
user_info = {
        'first': 'igor',
        'last': 'qwetrty',
        'location': 'moscow',        
        }
users['migor'] = user_info

for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())
    

    



