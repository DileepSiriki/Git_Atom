class MyClass():
     def __init__(self):
             self.__superprivate = "Hello"
             self._semiprivate = ", world!"

mc = MyClass()
print(mc._MyClass__superprivate)
print(mc.__dict__)
print(mc._semiprivate)
print(dir(mc))


mes="dil"
print('mes''eep')
print("mes")

name="dILleep"
#print(title(name))
print("kohIl".title())

print("dileep")
x="io"
print(f"{x.title()}")

print("hi",2+3)

print(2,"hi",5mi)

l=[1,2,3]
print(l[2.0])

a,b="di","od"
c=f"{a}{b}"
print(f"hi {a=} hii {b!=}")
print(f"{a} leep {b}c {c} e")

a="python"
b="java  "
print(a)
print("Languaga %s is better tahn %s " %(a,b))
print("languagae {0} ia better than {1}".format(a,b))
print("a={0},b={1}".format(b,a))
print("{na
me} {another}".format(name=a,another=b))

foo="bar"
print(f"{foo             = }")
print(f"\t {foo}")

age=14_12_000
print(age)

import datetime
today=datetime.datetime.today()
print(today)
print(f"{today:%B  %d, %Y}")


str='''dileep'''
print(str)
str1='str'
print(str1)

tup2=(1,2)
x,y=tup2
print(x,y)

b=true
print(b)
print("\\\\\\di")
a='d'
b='g'
c=a+b
print(c,type(c),type(b))

print("name".isalnum())

p=3,4
print(p)
str1=str('str')
print(str)

k=['a','b','c']
 del k[1]
print(a)
m=k.pop()
print(m)


2="gae"
print(2)
print(2+3==4+4)
print(f"which is greater {2+3 != 3+4}",5+6)

d='dhoni'
e="dhoni"
f='''dhoni'''
g="""dhoni"""
print(d,e,f,g)
print(round(20.09))
str=123
print(str'str')

a=10
b=a-3
print(b)

str="dhoni"
print("my favis {1} and {0}".format(str,'raina'))

val=raw_input("enter a value :")
print(val)
val = input("Enter your value: ")
print(val)
name = input("Enter your name: ")
print("Hello " + name)


list=[0,1,2,3,4,5,6,7,8,9,3,4,5]
print(list)
list[2]='dhoni'
print(list)
list.remove(3)
print(list)
popped=list.pop(4)
print(f"popped element is {popped}")
print(list)
del list[6]
print(list)
list.append('dileep')
print(list)
list.insert(3,'sakshi')
print(list)
#list1=str(list)
#list.sort()
print(f"sorted list is : {list1}")
print(iter('a'))



a="dileep  is a      good boy"
list=list(a)
print(list)

squares=[]
for i in range(10):
    value=i**2
    squares.append(value)
print(squares)


s="fih"
s[1]='k'
print(s)

s1=[]
s=['1','dhoni','3','4','5',[3,4,5],6]

print(s[5)

s1=s.copy()
print(s1)
s[len(s):]=[6]
s.append([8])
print(s)



for i in s :
    s1.append(i)
print(s1)
s.pop()
print(s,s1)
print(f"{s[1].title()}")


s[2:4]='e'
print(s)

a,b,c,d,e=(1),('1'),[1],['1'],(1,)
print(type(a),type(b),type(c),type(d),type(e))

a=(1,2,3,4,5,6)
del a[2]
print(a)
a[len(a):]='f'
print(a)

b=('a','b','c','d')
c=(7,8,9,'e','f','g')

a=[1,2]
b=[3,4]
c=a.copy()
print(c)
c.pop()
print(a,c)

a={1,2,1,3}
print(a,type(a))
a.update('e')
#a[1]='e'
print(a)


num=[1,2,3,4,5,6,7]
#even=odd=[]
even=[]
odd=[]
for i in num :
    if( i%2 == 0 ):
        #print(f"the even numbers are : {i}")
        even.append(i)
    else :
        #print(f"{i} is odd")
        odd.append(i)
print(f"{even , odd}" ,sep="\n" )

a,b=1,2
if a<5 and b>0 :
    print("yayy")

a={'a':100 , 'b':200}
print(a['b'])

alien_0={"x_pos":0,"y_pos":2,"speed":'medium'}
print(f"current position  of alien_0 is :{alien_0['x_pos'],alien_0['y_pos']}")
if alien_0["speed"] == "medium" : alien_0["x_pos"]+=1 ;print(alien_0)

a,b,c=true,True,TRue
print(type(a,b,c))

def printing(name):
    print(f"my name is {name}")
printing('dileep')

print(type(2))


class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def sit(self):
        print(f"I am {self.name} and i am {self.age} old !!")

p1=person('dileep',27)
p2=person('dhoni',40)
print(p1.name)




details=[{'no':1111,'pin':111,'bal':30000},{'no':2222,'pin':222,'bal':30000},{'no':3333,'pin':333,'bal':30000}]

for detail in details :
    print("welcome to SBI-ATM !!!")


import sys
print(sys.path)
for module in sys.modules:
    print(module,sep="\n")
print(sys.modules)

from .Testing import pizza
pizza(8,'a','b','c')

import Testing
Testing.pizza(8,'a','b')

print('a'+'b')
a='c'
b='d'

print(a*5,b)
print(a,'bcd')

a='dileep'
a=a[0:2]+'m'+a[3:300] ; print(a)
a[2]='k'
print(a)




class dog:
    breed="animal"
    def __init__(self,name,age):
        self.n=name
        self.a=age

obj1=dog('jan',19)
print(obj1)
print(obj1.n,obj1.a)

a=11;print(type(a))
b=str(11) ; print(type(b)) ; c=int(b);print(type(c))
===9-========================================llllllllllllllllll


s="dileep"
print(s[::-1])

k=len(s)
for c in s :
    print(s[k-1],end="")
    k=k-1
print('\n')

k=list(s)
print(''.join(reversed(k)))

#fact(5)=5*4*3*2*1
sum=0
def factorial(x):
    while(x >= 2):
        print(f"computing fact of {x}")
        sum=sum+(x*factorial(x-1))
        print(sum)

factorial(5)


def fact(x):
    if(x==1) :
        return x
    else :
        return x * fact(x-1)
k=fact(5)
print(k)


from datetime import datetime
now=datetime.now();print(now)
print(now.strftime("%m-%y %H%S"))

import datetime
import time
while True:
    a=datetime.datetime.now()
    print(a.strftime("%H-%M-%S"))
    time.sleep(1)


import sys
import time

for i in range(10):
    print(i)
    time.sleep(1)

print("d")

######################################################################
######################################################################

a='a'
b='b'
c=4

print(a+b)
print(a+"money")
print(b,"money")
print(2+4)
print("strings are %s and %s" %(a,b))
print(type(c))

str="awesome"
def call():
    print("python is " + str)
call()

print("abc"*10)

print(encode("dileep"))
print("dileep".encode())

a="dhoni"
print(a[2])
print(a[2:10])
print(len("dhoni"))



a="kumar"
print(len(a))
print(a[len(a)-1])
print(a[4:1:-1])
print(a[len(a)::-1])
b=a[len(a)::-1]
print(a,b)
print(a[0:2],'z',a[3:])
print(a[len(a):0:-1])
print(a[2])
print ('dileep')

a='1'
b='2'
print(a+b)
print("dileep is ",a )
print("dileep  is"+b)
c=a+b
print(c)
d=a+b+'k'
print(d)

print(2+2)

a=''' speed \
def
'''
print(a)

a='a'
b='b'
print('first alphabet is %s and next comes %s' %(a,"x"))

a,b,c='f','g','h'
print(a,b,c)
print(a*20,"dhoni")

a,b="dileep","kumar"
print(f"I am {a}{b}")
c=f"I am {a}{b}"
print(c)

a=10
print(id(a))

a="dhoni"
print(reversed(a))
print(list(reversed(a)))
print(' '.join(list(reversed(a))))
print(" ".join(a))


print(a)
print(a.capitalize())
print(a.find("a"))
d=a.split(sep="o")
print(d,"hi")

a='dileep'
b='kumar'
print("hi %s%s" %(a,b))
print("hi {}{}".format(a,b))
print(f"hi {a}{b}")
print("hi {x}{y}".format(x=a,y=b))

m="hello world !!!"
def rev():
    print(m[::-1])
rev()

def rev1():
    i=1
    while(i<=len(m)) :
        print(m[-i],end="")
        i=i+1
rev1()


thislist = ["zaw", "apple", "banana", "cherry", "orange","apple", "kiwi", "melon", "mango"]
thislist.append("dhoni")
print(thislist)
print(thislist.index("apple"))
print("apple" in thislist)
print(list(reversed(thislist)))
print("@".join(list(reversed(thislist))))
print(thislist[len(thislist)-1])
print(thislist.pop(2))
print(thislist)
del thislist
print(thislist)

thislist = ["zaw", "apple", "banana", "cherry", "orange","apple", "kiwi", "melon", "mango"]
print(len(thislist))
thislist.pop()
print(len(thislist))

print(thislist)

a=[1,2]
b=a.copy()
print(a,b)

c=[1,1,2,2,3,5,1]
print(set(c))

def pets(type, name):
    """This function is used to get pet details """
    print(f"I have a {type} and I call it {name}")
pets("dog","bill")
print(pets.__doc__)


name = lambda a : a + [2]
a=[1,2,3]
print(name(a))


k="dhoni has a dog"
a=k.split("o")
print(a)
print(";".join(a))


a="doni"
print(a[::-1])


a,b=1,2
if(a==1 and b==2):
    print("yay")
else:
    print("ik")

for(i=1;i<=10;i++)
    print(i)

for i in range(1,10):
    print(i)

=====================

num=100

for i in range(1,num):
    count=0
    for j in range(1, i+1):

        k=i%j
        #print(i,j,k)
        if(k==0):
            count=count+1
    #print(i,"count is ",count)
    if(count<=2):
        print(i)

fact=1
num=100
for i in range(1,num+1):
    fact = fact*i
print(fact)

num=100
factorial=1
for i in range(1,num + 1):
       factorial = factorial*i
print(factorial)


lower = 100
upper = 2000

for num in range(lower, upper + 1):

   # order of number
   order = len(str(num))

   # initialize sum
   sum = 0

   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10

   if num == sum:
       print(num)

# Python program to shuffle a deck of card

# importing modules
import itertools, random

# make a deck of cards
deck = list(itertools.product(range(1,14),['Spade','Heart','Diamond','Club']))

# shuffle the cards
random.shuffle(deck)

# draw five cards
print("You got:")
for i in range(5):
   print(deck[i][0], "of", deck[i][1])



a,b=0,1
num=50
count=0
while(count<num):

    c=a+b
    print(c)
    a=b
    b=c
    count=count+1



def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = 50

# check if the number of terms is valid
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(recur_fibo(i))


def fib(n):
    if n<=1:
        retirn 1
    else:
        return fib(fib(n-1)+fib(n-2))
