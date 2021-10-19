#converting from dec to binary only
def binary(n):
    if n>1:
        binary(n//2)
        print(n%2,end="")
dec = int(input("enter a value: "))
binary(dec)

#converting from dec to others like; bin,hex,oct

dec = int(input("enter a value : "))
print("the decimal of ",dec,"is:" )
print(bin(dec),"in binary")
print(oct(dec),"in octal")
print(hex(dec),"in hexadecimal")


# determining power of certain amount of terms
terms = int(input("total term:"))
result = list(map(lambda x:2**x,range(terms)))
for i in range(terms):
    print("2 ^",i,"is",result[i])



#multiplication table
num = int(input("enter a value: "))
for i in range(0,11):
    num+=1
    i+=1
    print(num,"x",i,"=",num*i)

# to determine which number is larger or smaller


num = float(input("enter value: "))
num1 = float(input("enter value: "))
num2 = float(input("enter value: "))
if num>=num1 and num>=num2:
    print("the largest number is",num,"cause it's the largest")
elif num1>=num and num1>=num2:
    print("the largest is",num1,"cause it's the largest")
else:
    print("the largest is:",num2,"cause it's the largest")

if num<num1 and num<num2:
    print("the smallest is :",num)
elif num1<num and num1<num2:
    print("the smallest is:",num1)
else:
    print("the smallest is:",num2)


