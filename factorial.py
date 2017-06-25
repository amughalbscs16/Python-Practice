#Trying Python for the First Time Writing Simple functions and stuff.

def factorial1(number):   #1 Tab = Start Definition/Body of Function/for/if/while or other conditionals.
    factorial=1;
    while (number>0):
        factorial=number*factorial;
        number-=1
    print(factorial)
    return factorial

factorial1(5)          #Calculate Print By Function Call.
print(factorial1(5))   #Calculate Print using return
