#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Answer no 1
n = int(input())
divBy7 = [i for i in range(0,n) if (i % 7 == 0)]
print(divBy7)

def divCheck(n):
    for i in range(n):
        if i % 7 == 0:
            value = True
        else:
            value = False
        print(i,value)
        
divCheck(n)


# In[ ]:


#Answer no 2
import operator
text_line = input("Type in:")
freq = {}

for i in text_line.split(' '):
    if i.isalpha():
        if i not in freq:
            freq[i] = 1
        elif i in freq:
            freq[i] = freq[i]+1
            
    else:
        pass
    
sorted_freq = sorted(freqitems(), key = operator.itemgetter(0))
print(sorted_freq)

for i in sorted-freq:
    print(i[0],i[1])


# In[4]:


#Answer no 3
class person:
    gender = "Gaurav"
    def getGender(self):
        print("Hi! i am %s"%self.gender)
        
class Male(person):
    gender = "male"
    
class Female(person):
    gender = "female"
    
a = Male()
b = Female()

a.getGender()
b.getGender()


# In[5]:


#Answer no 4
subjects = ["I","You"]
verbs = ["Play","Love"]
objects = ["Hockey","Football"]
for i in range(len(subjects)):
    for j in range(len(verbs)):
        for k in range(len(objects)):
            sentence = "%s %s %s."%(subjects[i],verbs[j],objects[k])
            print(sentence)


# In[9]:


#Answer no 5
import zlib
a = "this string needs compressing"
a = zlib.compress(a.encode())
print(zlib.decompress(a))


# In[10]:


#Answer no 6
import math
def binarySearch(li,ele):
    lowest = 0
    highest = len(li)-1
    index = -1
    while highest>+lowest and index == -1:
        mid = int(math.floor((highest+lowest)/2.0))
        if li[mid]==ele:
            index = mid
        elif li[mid]<ele:
            highest = mid-1
        else:
            lowest = mid+1
            
    return index
sortedList = [2,5,7,9,11,17,222]
print(binarySearch(sortedList,11))


# In[ ]:




