#!/usr/bin/env python
# coding: utf-8

# In[6]:


s= "sudh"


# In[7]:


s+str((1))


# In[8]:


s*4


# In[10]:


#In-built Function
s.upper()


# In[11]:


a= "SUdh"


# In[12]:


a.lower()


# In[16]:


a="sudh kumar "


# In[5]:


type(a.split()) #split() always return a list
#defaultly takes white space


# In[20]:


a="sudh@kumar@wooo"


# In[23]:


a.split("@") #Pass deliminiter for spliting 


# In[3]:


a="sudhAfsAhh"
a.split("A")


# In[7]:


#Equivalent of split() i.e., partition()
type(a.partition("A")) #Always looks for separater or argument 
#returns tuple


# In[8]:


d="sfasfdfsadfsafsfsaf"


# In[10]:


d.find("a") #only first ocurrence of the dilimin.. or charac. return we pass


# In[13]:


#if the specific charcater
#not in string return -1
d.find("3")


# In[14]:


f="sudh"


# In[20]:


f.center(20,"v") #always pass single charac..


# In[22]:


"sudh\tkumar".split('\t')


# In[26]:


#expandtabs()

"sudh\tkumar\tsfsds".expandtabs()


# In[25]:


#Format() function - 1

"My name is {} Kumar ".format("Amit")


# In[29]:


#Format() function - 2

a=input("please enter your name\n")
b=input("please enter your Lastname\n")

"my name is {} {} ".format(a,b)


# In[62]:


s="23234"


# In[63]:


#The isalnum() method returns True if all the characters are alphanumeric, meaning alphabet letter (a-z) and numbers (0-9).

#Example of characters that are not alphanumeric: (space)!#%&? etc.

s.isalnum()


# In[64]:


s.isalpha()


# In[65]:


s.islower()
#s.isupper()


# In[68]:


#The istitle() method returns True if all words in a text start with a upper case letter, 
#AND the rest of the word are lower case letters, otherwise False.

s.istitle()


# In[70]:


s.endswith('4')


# In[122]:


a = [1,2,3,4,5,"hello","sudh",4.56,[3,4,5]]
b = [4,6,7,8,"my","name"] 


# In[123]:


m = []
for i in a:
    m.append(i)
m    


# In[124]:


(a+b)*0


# In[125]:


b = [4,6,7,8,"my","name"] 


# In[126]:


b + list("hey")


# **Problem with list is it returns sepratable values or letters**

# In[127]:


b.append("hey")
b


# In[128]:


#insert(): If you want to add data in between
#whereas append() use to append at the tail or last of the data


# In[129]:


#Insert object before index

b.insert(-1,"Fab!")


# In[130]:


b


# In[131]:


b.insert(-2,"yes!")


# In[132]:


b


# In[133]:


b.pop() #remove data from very last index permanently


# In[134]:


b.pop(2)


# In[141]:


b[::-1] # not a permanent changes


# In[142]:


b.reverse() #it's a permanent change


# In[143]:


b


# In[144]:


b.sort()


# **-Always remember whenever use sorting either use numeric or string values**

# In[187]:


n = [4,8,7,6,10]


# In[188]:


n.sort(reverse=True) #desc..


# In[189]:


n


# In[190]:


n=["e","i","d"]


# In[191]:


n.sort()


# In[192]:


n


# In[211]:


a = [3,4,5,6,7]
b = [56,6,7,89,8]
c = [2,3,4,5,6,7,8,8,9,0]

d = [a,b,c]
d


# In[212]:


d[-1][::2] #steps taken 2 


# In[213]:


m = []
d = d[::-1]
for b in d :
    m.append(b[::-1])
m   
#or 
#m = []
#d.reverse()
#for b in d :
#    m.append(b.[::-1])    


# In[218]:


#Extracts data from all of the second position

n = []
for i in m:
    n.append(i[2]*2)


# In[219]:


n


# In[223]:


[{i[2]*2} for i in m ] #By just single line called "List Comprehension"


# In[226]:


s=[1,3,4,5,5]


# In[227]:


s.append([3,4,5,6])
s #append as it is


# In[232]:


m = [4,5,6,7,"dfd"]
m.extend([5,3,2,[6,7,8,"ds"]])  #it first unrap the data


# In[235]:


m #so only unwrap the first one


# In[242]:


m.index(6)


# In[243]:


m.find()


# In[245]:


#incase of list alternate for find()
m.index(2)

