# if else statement
name = 'Sujan'
if name == "Sujan":
	print('Hi Sujan')
print('Hello')

## gives hi sujan as output as the name variable is 
# goes into the if satatement and prints hello 
# if the name is provided any other on the veriable then 
# the condition would not be checked in if 


# else statement

password = 'welcome'

if password == 'welcome':
	print('Access granted')
else:
	print('Wrong password')

# gives access granted as  output as the variable password is matched
# gives wrong password when the varibale assign gets wrong


name = 'sujan'
age = 25
if name == 'Rohan':
	print('hello Rohan')
elif age < 12 :
	print('You are not like sujan.')
elif age > 30 :
	print('unlike you are not as sujan')
else:
	print('You did not enter a correct name')
