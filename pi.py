import math
import random
def IsInCircle(x,y):
    return (x*x + y*y) < 1

repeat = int(input())
def Find():
    NUM_IN_CIRCLE = 0
    NUM = 1
    pi = 0
    while True:
        if abs(math.pi - pi) > 0.01: 
            if IsInCircle(random.choice([1,-1]) * random.random(),random.choice([1,-1]) * random.random()):
                NUM_IN_CIRCLE +=1
        else:
            break
        NUM +=1
        pi = 4 * NUM_IN_CIRCLE / NUM
    return pi,NUM

sum = 0
for i in range(repeat):
    a,b = Find()
    sum +=a
    # print(a,b)
print('average is: {}'.format(sum/repeat))