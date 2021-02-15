""" In a given list of elements, all elements are equal except the one.Write a code to find the odd man out (Stray number)"""
def odd_man_out(mylist):
    mylist.sort()
    length=len(mylist)
    if(mylist[0]==mylist[1]):
        return mylist[length-1]
    else:
        return mylist[0]



"""---------------------------------------------------------------------"""
"""In a given list of elements, find the elements which is close to its mean """
def mean_close(mylist):
    mean=sum(mylist)/len(mylist)
    length=len(mylist)
    for i in range(1,length):
        if(mylist[i]>mean):
            return mylist[i],mylist[i-1]


"""----------------------------------------------------------------"""
""" Find the average speed of vehicle, given the distance travelled for fixed time intervals, e.g. [0, 0.1, 0.25, 0.45, 0.55, 0.7, 0.9, 1.0]"""
def average_speed(mylist):
    return sum(mylist)/len(mylist)


"""--------------------------------------------------------------------------"""
"""Find the no.of people in a bus, given the data of people onboarding & alighting at each station"""

def no_of_people_in_bus(mylist_on,mylist_off):
       return sum(mylist_on)-sum(mylist_off)


"""--------------------------------------------------------------------"""
""" Find the missing number, given the original list and modified one"""
def missing_no(mylist_org,mylist_modi):
          return (set(mylist_org)-set(mylist_modi))


"""-------------------------------------------------------------"""
""" Find the ifference between two lowest numbers in the list"""
def sum_lowest_two(mylist):
    mylist_sort=mylist.sort()
    ans =mylist_sort[0]-mylist_sort[1]
    return ans

"""-------------------------------------------------------------------"""
""" In a given list, count no.of elements smaller than their mean"""
def smaller_then_mean(mylist):
    mean=sum(mylist)/len(mylist)
    count=0
    for i in range(0,len(mylist)):
          if(mylist[i]<mean):
              count+=1
    return count

