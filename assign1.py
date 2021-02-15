"""1) Biggest of three/four numbers"""
def max_no(numbers):
    print(max(numbers))
numbers=[]
n=int(input("enter no of elements!"))
for i in range(0,n):
    numbers.append(int(input()))
max_no(numbers)

"""--------------------------------------------------------------------------------"""

"""2)Check if given number is armstrong or not"""
def armstrong_no(number):
    arm=0
    length=len(number)
    for x in number:
       arm+=(int(x)**length)
    if(int(number)==arm):
        return "yes"
    else:
        return "no"

number=input("enter a no")

result=armstrong_no(number)
print(result)
"""----------------------------------------------"""
"""3) Reverse the number, sum of digits"""
def reverse_number(number):
   mylist=[int(x) for x in number]
   mylist_rev=mylist[::-1]
   string=""
   for i in mylist_rev:
        string+=str(i)
   return string
number=input("enter a number")
result=reverse_number(number)
print(result)

"""---------------------------------------------------"""
"""4)sum of digits"""
def add_digits(number):
    addition=0
    for x in str(number):
        addition+=int(x)
    return addition
number=input("enter a no.")
result=add_digits(number)
print(result)

"""--------------------------------------------------"""
"""5)GCD/HCF of two numbers"""
def hcf(no1,no2):
    gcf=0
    bigger=max([no1,no2])
    for i in range(1,bigger):


"""---------------------------------------------------"""
"""6)LCM without computing GCD/HCF"""
   def lcm(no1,no2):
    for i in range(2,no1):
        if no1%i==0 and no2%i==0:
            lcm=i
            break
    return lcm

"""-----------------------------------------------------------------"""
"""7)Check if given year is Leap year or not """
def leap_year(num):
    if(num%400==0):
       return True
    if(num%4==0 and num%100!=0):
       return True
    else:
        return False 


"""-------------------------------------------------------------------------"""

""""""
def add_digits(number):
    addition=0
    for x in str(number):
        addition+=int(x)
    return addition
number=input("enter a no.")
result=add_digits(number)
print(result)

"""--------------------------------------------------------------------"""
"""8)Type of triangle - equilateral, isosceles, scalene, right angled"""
def  check_tri(side1,side2,side3):
        if(side1==side2==side3):
            return "equlatral trio";
        if(side1==side2 or side2==side3 or side3==side1):
            return "isoceleles trio"
        if(side1!=side2!=side3):
            if((side1**2+side2**2==side3**2) or (side2**2+side3**2==side1**2) or(side3**2+side1**2==side2**2)):
                return "right angle trio" 
            else:
                return "scalene trio"      


"""-------------------------------------------------------------"""
"""9)Roots of a quadratic equation"""
def roots_of_eq(a,b,c):
    root1=(-b+(b**2-4*a*c)**(1/2))/(2*a)
    root2=(-b-(b**2-4*a*c)**(1/2))/(2*a)
    return root1,root2

"""-----------------------------------------------------------------"""
"""10)Quadrant of a given point (x,y) """
def quardrant(X,Y):
    if(X==0 and Y==0):
        return "origin"
    if(X==0):
        return "oN Y AXIS"
    if(Y==0):
        return "ON X AXIS"
    if(X>0 and Y>0):
        return "first"
    if(X>0 and Y<0):
        return "four"
    if(X<0 and Y>0):
        return "second"
    if(X<0 and Y<0):
        return "third"

"""-------------------------------------------------------------------"""
""" 11)Choice based arithmetic"""
def choice_arithmatic(no1,no2,choice):
    if(choice=="add"):
        return no1+no2
    if(choice=="mul"):
        return no1*no2
    if(choice=="sub"):
        return no1-no2
    if(choice=="div"):
        return no1/no2

"""------------------------------------------------------------------------"""
"""12) Fibonacci sequence"""
def fab(a,b,no):
     for i in range(2,no):
        c=a+b
        print(c)
        a=b
        b=c

"""------------------------------------------------------------"""
"""13)Tribonacci series"""
def tribonacci(a,b,c,no):
     for i in range(3,no):
        d=a+b+c
        print(d)
        a=b
        b=c
        c=d

"""------------------------------------------------------------------------------"""
"""14)Factorial of a given number"""
def factorial(no):
    fact=1
    i=no
    while(i>0):
        fact*=i
        i-=1
    return fact

"""---------------------------------------------------------------------------------"""

"""15) Sum of the factors, n=30, 1+2+3+5+6+10+15"""
def sum_factors(no):
    sum=0
    for i in range(1,no+1):
        if(no%i==0):
          sum+=i
    return sum



"""-----------------------------------------------------------------------------------"""
"""16)Check if given character is vowel or consonant"""
def vowel_check(ch):
    if(ch.upper()=='A' or ch.upper()=='E' or ch.upper()=='I' or ch.upper()=='O' or ch.upper()=='U'):
        return "vowel"
    else:
        return "consonent"


"""-----------------------------------------------------------------------------------"""
"""17)Digital root of a given number, 7895 -> 29 -> 11 -> 2 """
def digital_root(n):
    if(len(n)==1):
        return n
    else:
        add=0
        for i in range(0,len(n)):
            add+=int(n[i])
            digital_root(add)


"""-------------------------------------------------------"""
""" 18)List/count of prime numbers for given range"""
def prime_no(n):
    mylist=[]
    for i in range(2,n+1):
       for j in range(2,i):
        if(i%j==0):
            break
        else:
            mylist.append(i)
    return mylist


"""------------------------------------------------------------"""
""" 19)Sum of triangular numbers, n=4, 1 + (1+2) + (1+2+3) + (1+2+3+4) = 20"""
def triangular_nos(n):
    add1=0
    for i in range(1,n+1):
        add=0
        for j in range(1,i+1):
          add+=j
        add1+=add
    return add1


"""---------------------------------------------------------------------"""
"""26)No.of combinations for n teams to play each other,  i.e. nCr"""
def teams(n):
    return (n*(n-1))/2

"""----------------------------------------------------------------------------"""
"""super prime no"""
def XYZ(n, isPrime): 
        isPrime[0] = isPrime[1] = False
    for i in range(2,n+1): 
        isPrime[i] = True
   
    for p in range(2,n+1): 
       
        if (p*p<=n and isPrime[p] == True): 
            
            for i in range(p*2,n+1,p): 
                isPrime[i] = False
                p += 1
def sup_Prime(n): 
    
    isPrime = [1 for i in range(n+1)] 
    XYZ(n, isPrime) 
    primes = [0 for i in range(2,n+1)] 
    j = 0
    for p in range(2,n+1): 
       if (isPrime[p]): 
           primes[j] = p 
           j += 1. 
    for k in range(j): 
        if (isPrime[k+1]): 
            print primes[k], 
