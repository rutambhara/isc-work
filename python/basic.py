import numpy as np
a='blah'
print a

b=6
c=10
d=b+c

print d

mylist = [23,"hi",2.4e-10]
count=0
while count <2:
    item=mylist[count]
    print item, mylist.index(item)
    count+=1

for x in mylist:
    print x, mylist.index(x)

mylist2=[1,2,3,4,5]

slicing=mylist2[1:5]
print slicing

forward=[]
backward=[]
values=["a","b","c"]
for item in values:
    forward.append(item)
    backward.insert(1,item)
print forward
print backward

countries=["UK","USA","UK","UAE"]
dir(countries)

print dir(countries)

t=(2,)
print t[-1]
l=range(100,201)
print l
tup=tuple(l)
print tup[0],tup[-1]
with open ("weather.csv","r") as reader:
    data=reader.read()
print data

s="I love to write python"
split_s=s.split()
print split_s
for x in split_s:
    print x
  #  if x.find("t") > -1:
       # print "I found 't' in: '{0}'".format(x)

def greet(name):
    temp='hello'+name
    print temp

greet("tom")

def double_it(num):
    return 2 * num

print double_it(2)

band=["mel","geri","victoria","mel","emma"]
counts={}
for name in band:
    if name not in counts:
        counts[name]=1
    else:
        counts[name]+=1
for name in counts:
    print name,counts[name]

def calmag(u,v, minmag = 0.1):
    mag = ((u**2)+(v**2))**0.5
    output=np.where(mag>minmag,mag,minmag)
    return output
u=np.array([[4,5,6],[2,3,4]])
v=np.array([[2,2,2],[1,1,1]])
print calmag(u,v)

import numpy.ma as MA
marr=MA.masked_array(range(10),fill_value=-999)
print marr, marr.fill_value
marr[2]=MA.masked
print marr


