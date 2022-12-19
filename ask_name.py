# this program says hello and asks for my name and age

print('Hello world!')

print('What is you name ?') #ask for their name
myName = input()
print('It is good to meet you, ' + myName)
print('The length of your name is :')
print(len(myName))

print('What is your age ? ') #ask for ages
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year later.')