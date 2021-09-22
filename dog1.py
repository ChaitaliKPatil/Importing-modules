#Start a new Python module by defining a function that supplies a default string value to its argument for display
#This is a module named 5 cat1 to be imported in the other scripts to use these functions directly without copying the code in each script file.
print('This is a module named cat1 to be imported in the other scripts to use these functions directly without copying the code in each script file.')
def bark(pet='A Dog'):
    print(pet,'Says WOOF!')
# add two more function definitions that also supply default string values to their arguments for display 
def lick(pet='A Dog'):
    print(pet,'Drinks Water.')
def nap(pet='A Dog'):
    print(pet,'Sleeps in the sun!!')




