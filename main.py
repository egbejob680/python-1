#printing numbers from 1-20
for i in range(0,20):
    i+=1
    print(i)

#odd numbers less than 100
for i in range(0,100):
    if i%2!=0:
        print(i,"is odd")
    elif i==100:
        print("")
    else:
        print("")
#even numbers less than 100

for i in range(0,100):
    if i%2==0:
        print(i,"is even")

    else:
        print(" ")

# multiplication table with 7
num = 7
for i in range(0,20):
    result=num*i
    print(num,"x",i,"=",result)

# calculating hcf

def hcf(x,y):
    if x>y:
        smaller = y
    else:
        smaller = x
        for i in range (1,smaller+1):
            if((x%i==0) and (y%i==0)):
                hcf=i
    return hcf
num1 = int(input("enter first;"))
num2 = int(input("enter sec"))
print("the hcf between",num1 ,"and",num2,"is",hcf(num1,num2))








