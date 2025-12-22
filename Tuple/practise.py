'''
1. Find max and min element in tuple
'''

t=(4,2,9,1)

max_val=min_val=t[0]

for num in t:
    if num>max_val:
        max_val=num
    if num<min_val:
        min_val=num
    
print(max_val,min_val)


'''
2. Count the occurence of an element
'''

t=(1,2,2,3)
x=2

count=0

for num in t:
    if num==x:
        count=count+1

print(count)

'''
3. Convert the tuple to list and modify.
'''

t=(1,2,2,3)

list1=list(t)
list1.append(4)

t=tuple(list1)
print(t)


'''
4. Unpack a tuple
'''

t=(10,20)

a,b=t
print(a,b) 