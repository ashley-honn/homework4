#write a Boolean function prime which takes an integer as an argument and returns true
#if argument is a prime number, or false otherwise


def prime(number):

    count = 0

    for a in range (1,number+1):
        prime = number % a
        if prime == 0:
            count += 1
        else: count = count
        a += 1

    if count == 2:
        return True
    elif count > 2:
        return False


import random 

#this is for the random 6 digit number generator
for a in range (0,6):
    number = random.randrange(0,100)
    if prime(number):
      if prime(number) == True:
        print('The random number ' + str(number) + ' is a prime number.')
    elif prime(number) == False:
        print('The random number ' + str(number) + ' is not a prime number.')
