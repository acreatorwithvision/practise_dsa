'''
1. Reverse an Array in place
this method should not use slicing as it will create a new list and also not create or add elements into another array as it will violate the rule.
'''

arr=[1,2,3,4,5]

left=0
right=len(arr)-1

while left<right:
    arr[left],arr[right]=arr[right],arr[left]
    left+=1
    right-=1

print(a)



'''
2. Second maximum element in an array.
This should return the second maximum element in an array without creating another array.
'''

arr=[10,5,20,8]

largest=smallest=-10**9

for num in arr:
    if num>largest:
        second=largest
        largest=num

    elif num>second and num!=largest:
        second=num

print(second)

