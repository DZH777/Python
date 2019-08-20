with open('pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents)
print('----------------')
filename = 'pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
print('----------------')
with open(filename) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip())
print('----------------')
pi_string = ''
for line in lines:
    pi_string += line.rstrip()
print(pi_string)
print(len(pi_string))

print(pi_string[:5] + "...")
print(len(pi_string))

filename = 'pi_digits_max.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.rstrip()
print(pi_string[:50] + "...")
print(len(pi_string))    
birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")
    
message = "I really like dogs."
print(message)
print(message.replace('dog', 'cat'))


