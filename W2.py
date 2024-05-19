import random

#1
print("Practice 1")
def randoMachine():
    sum = []
    for i in range(10):
        sum.append(random.randrange(1,50,1))
        i+=1
    return(sum)    

num = randoMachine()
print(num)


#2
print("Practice 2")
def squareSum(n):
    sum2 = 0
    for i in range(10):
        sum2 = sum2 + int(n[i])**2
        i+=1
    print("This is the result : " + str(sum2))
    
squareSum(num)