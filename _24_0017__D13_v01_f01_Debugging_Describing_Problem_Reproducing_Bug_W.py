#This is intentional that these will not run sometimes. This day is for debugging:

# Describe Problem
def my_function():
    for i in range(1, 20):
        if i == 20:
            print("This is function1: You got it")
my_function()

def my_function2():
    for i in range(1, 21):
        if i == 20:
            print("This is funtion2: You got it")
my_function2()
#20 is not included, you would want to make it 0-20 or range(1-21), and this will only print once.


# Reproduce the Bug
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 6)    #We can replace the value of randint(1, 6) with = 6 to test a specific number (0, 1, or 6 to test out the range error. This tests both ends of the range
print(dice_imgs[dice_num])
#randint needs to be (0, 5) and not (1,6) #the error happened with most numbers less than 3.
