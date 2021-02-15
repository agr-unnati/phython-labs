
#Check whether given string is isogram or not
def isomer(a):
    return len(a) == len(set(a.lower()))

#Compute the word frequency in given message

def word_count(str):  
    wds = str.split()
    c = dict()
    for w in wds:
        if w in c:
            c[w] += 1
        else:
            c[w] = 1

    return c


#Given a number, find the largest number by shuffling the digits

def max_num(inm):

    s = str(num)
    c = [0 for x in range(10)]
    for i in range(len(s)):
        c[int(s[i])] = c[int(s[i])] +  1
    r = 0
    mul = 1

    for i in range(10):
        while c[i] > 0:
            r = r + ( i * mul)
            c[i] = c[i] - 1
            mul = mul* 10
 
   
    return r
    #Convert ip address from "a.b.c.d" format into integer and vice versa
def ip(a):
    s=a.split('.')
    l=[]
    for i in s:
        l.append(int(i))
    print("The inter for ip address is:")
    return l

def integer():
    l=make_list()
    list1=[]
    for i in l:
        list1.append(str(i))
    print(list1)
    x='.'.join(list1)
    print("The ip address for integer is :")
    return x
#Given a string, find the mexican wave
def wave(a):
    l=[]
    for i,j in enumerate(a[:]):
        u=a[i].upper()
        b=a[:i]+u+a[i+1:]
        l.append(b)
    print("The mexican wave:")
    return l
#Correct the malformed time string , for e.g "5:70:65" to "6:11:05"
def time(a):

    l=a.split(":")
    l1=[]
    for i in l:
        l1.append(int(i))
    

    if l1[2]>60:
        l1[1]=l1[1]+1
        l1[2]=l1[2]-60
    
    if l1[1]>60:
        l1[0]=l1[0]+1
        l1[1]=l1[1]-60
    
    l2=[]
    for i in l1:
        l2.append(str(i))
    
    return ":".join(l2)
#Correct the malformed date string , for e.g. "45/8/2018" to "14/9/2018
def date(a):

    l=a.split("/")
    l1=[]
    for i in l:
        l1.append(int(i))
    

    if l1[0]>31:
        l1[1]=l1[1]+1
        l1[0]=l1[0]-31
    
    if l1[1]>12:
        l1[2]=l1[2]+1
        l1[1]=l1[1]-12
    
    l2=[]
    for i in l1:
        l2.append(str(i))
    
    return "/".join(l2)
# Generate accumulated strings,e.g. abcd ==> A-Bb-Ccc-Dddd
def accumulated(s):
    for i in range(1,len(s)+1):
        for j in range(0,i):
            print(s[i-1],end=" ")
            
        print("-",end=" ")
        
#RGB to Hex conversion and vice versa, e.g. (255,0,255) into 0xFF00FF

def rgb_to_hex(r, g, b):
    return '%02x%02x%02x' % (r, g, b)
rgb_to_hex(255, 0, 255)

def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i+lv//3], 16) for i in range(0, lv, lv//3))
hex_to_rgb("ff00ff")
