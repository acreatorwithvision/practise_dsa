'''
1. Check for duplicates
'''

nums=[1,2,3,4,2]

seen=set()

duplicate=False

for num in nums:
    if num in seen:
        duplicate=True
        break

    seen.add(num)
print(duplicate)


'''
2. Remove Duplicates
'''
nums=[1,2,2,3,1]

seen=set()
res=[]

for num in nums:
    if num not in seen:
        sen.add(num)
        res.append(num)

print(res)

'''
3. Intersection of 2 Arrays
'''

a=[1,2,3,4]
b=[3,4,5]

print(set(a)&set(b))

'''
4. Union of 2 Arrays
'''

a=[1,2,3,4]
b=[3,4,5]

print(set(a) | set(b))
