# make the “cat” module functions available
from dog1 import*
# call each function without supplying an argument
pet=input('Enter your pet\'s name:')
bark(pet)
lick(pet)
nap(pet)
#. Now, call each function again and pass an argument to each, then save the file
bark('Ramu')
lick('Ramu')
nap('Ramu')



