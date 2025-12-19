##Array/List

'''
1. Maximum element in an array

Given an array of integers, return the maximum element.
Constraints
1 ≤ n ≤ 10⁵
-10⁹ ≤ arr[i] ≤ 10⁹
Do not use built-in max()
'''

def max_array(arr):
    max=0
    m=arr[0]
    for i in range(1,len(arr)-1):
        if arr[i]>m:
            max=arr[i]
    return max


'''
2. Reverse an array in place

Reverse the array without using extra space.
Constraints
1 ≤ n ≤ 10⁵
'''
arr=[1,2,3,4,5]
left=0
right=len(arr)-1

if left<right:
    arr[left],arr[right]=arr[right],arr[left]
    left=left+1
    right=right-1
print(arr)

'''
3. Move all zeroes to end
Move all zeros to the end while maintaining order of non-zero elements.
'''

arr=[0,1,0,3,12]

idx=0

for i in arr:
    if arr[i]!=0:
        arr[idx]=arr[i]
        idx=idx+1

for i in range(idx,len(arr)):
    arr[i]=0

print(arr)

'''
4. Second Largest element

Return the second largest distinct element.
'''

arr[10,5,20,8]

largest=second=-10**9

for num in arr:
    if num>largest:
        second=largest
        largest=num
    elif num>second and num<largest:
        second=num

print(second)


