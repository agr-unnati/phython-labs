from assign1 import *

#1)Biggest of three/four numbers
numbers=[]
n=int(input("enter no of elements!"))
for i in range(0,n):
    numbers.append(int(input()))
max_no(numbers)
#2)Check if given number is armstrong or not
number=input("enter a no")

result=armstrong_no(number)
print(result)
#3)Reverse the number
number=input("enter a number")
result=reverse_number(number)
print(result)
# sum of digits
number=input("enter a no.")
result=add_digits(number)
print(result)

#GCD/HCF of two numbers
a =int(input("enter a no:"))
b =int(input("enter a no"))
if(gcd(a, b)):
    print('GCD of', a, 'and', b, 'is', gcd(a, b))
else:
    print('not found')
#LCM without computing GCD/H
no1=int(input("enter a no"))
no2=int(input("enter a no"))
result=lcm(no1,no2)
print(result)
#Given a number, find the largest numCF
no1=int(input("enter a no1"))
no2=int(input("enter a no2"))
result=lcm(no1,no2)
print(result)
#Check if given year is Leap year or not
num=int(input("enter a no"))
result=leap_year(num)
print(result)
#Type of triangle - equilateral, isosceles, scalene, right angled
side1=int(input("enter side 1"))
side2=int(input("enter side 2"))
side3=int(input("enter side
#Given a number, find the largest num 3"))
result=check_tri(side1,side2,side3)
print(result)
#Roots of a quadratic equation
a=int(input("enter a"))
b=int(input("enter b"))
c=int(input("enter c"))
result1,result2=roots_of_eq(a,b,c)
print(result1,result2)
#Quadrant of a given point (x,y)
X=int(input("enter X"))
Y=int(input("enter Y"))
result=quardrant(X,Y)
print(result)

#Choice based arithmetic
no1=int(input("enter NO1"))
no2=int(input("enter NO2"))
choice=input("add,mul,sub,div")
result=choice_arithmatic(no1,no2,choice)
print(result)
#Fibonacci sequence
no=int(input("enter a no"))
a=0
b=1
print(a)
print(b)0
print(result)
#Tribonacci series
no=int(input("enter a no"))
a=0
b=0
c=1
print(a)
print(b)
print(c)
result=tribonacci(a,b,c,no)
print(result)
#Factorial of a given number
no=int(input("enter a no"))
result=factorial(no)
print(result)

#Sum of the factors, n=30, 1+2+3+5+6+10+15
no=int(input("enter a no"))
result=sum_factors(no)
print(result)

#Check if given character is vowel or consonant
ch=input("enter a char")
result=vowel_check(ch)
print(result)



#Digital root of a given number, 7895 -> 29 -> 11 -> 2
n=input("enter a no")
result=digital_root(n)
print(result)
#List/count of prime numbers for given range
n=int(input("enter a no"))
result=prime_no(n)
print(result)
#Sum of triangular numbers, n=4, 1 + (1+2) + (1+2+3) + (1+2+3+4) = 20
n=int(input("enter a no"))
result=triangular_nos(n)
print(result)
#Maximum number by delenumbers=[]
n=int(input("enter no of elements!"))
for i in range(0,n):
    numbers.append(int(input()))
max_no(numbers)ting single digit in a 4 digit number
     5872  - 872,   9865 - 985
#Generate super prime numbers
n = 241
print("Sup_Prime less than or equal to ", n, " are :n", 
sup_Prime(n) ""
#No.of combinations for n teams to play each other,  i.e. nCr
n=int(input("enter no of teams"))
result=teams(n)
print(result)
#Generate number triangles/pyramids, pascal triangle
n=input("enter a number")
print(Pascal(n)) 