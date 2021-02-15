
#In a given list of elements, all elements are equal except the one.Write a code to find the odd man out (Stray number)
n=int(input("enter no elements in list"))
mylist=[]
for i in range(0,n):n=int(input("enter no of teams"))
result=odd_man_out(mylist)
print(result)

#In a given list of elements, find the elements which is close to its mean
no=int(input("enter no of elemnets of list"))
mylist=[]
for i in range(0,no):
    mylist.append(int(input("enter element")))
result1,result2=mean_close(mylist)
print(result1,result2)
#Find the average speed of vehicle, given the distance travelled for fixed time intervals, e.g. [0, 0.1, 0.25, 0.45, 0.55, 0.7, 0.9, 1.0]
no=int(input("enter no of elemnets of list"))
mylist=[]
for i in range(0,no):
    mylist.append(int(input("enter element")))
result=average_speed(mylist)
print(result)
#Find the no.of people in a bus, given the data of people onboarding & alighting at each station
no=int(input("enter no of stations"))
mylist_on=[]
mylist_off=[]
for i in range(0,no):
    mylist_on.append(int(input("no of people onboarded")))
for i in range(0,no):
    mylist_off.append(int(input("no of people onboarded")))
result=no_of_people_in_bus(mylist_on,mylist_off)
print(result)
#Find the missing number, given the original list and modified one
no=int(input("no of elements in list"))
mylist_org=[]
mylist_modi=[]
no=int(input("no of elements in list"))
mylist_org=[]
for i in range(0,no-1):
    mylist_modi.append(int(input("ele of modi list")))
result=missing_no(mylist_org,mylist_modi)
print(result)
#Find the ifference between two lowest numbers in the list
no=int(input("no of elements in list"))
mylist=[]
for i in range(0,no):
    mylist.append(input("ele of modi list"))
result=sum_lowest_two(mylist)
print(result)
#In a given list, count no.of elements smaller than their mean
no=int(input("no of elements in list"))
mylist=[]
for i in range(0,no):
    mylist.append(int(input("ele of modi list")))
result=smaller_then_mean(mylist)
print(result)
