'''
1. Stack Operations
'''

stack=[]

stack.append(10)
stack.append(20)

top=stack[-1]
print(top)

print(stack.pop)



'''
2. Reverse a string using stack
'''

s="hello"

stack=[]

for ch in s:
    stack.append(ch)

rev=""
while stack:
    rev=rev+stack.pop()

print(rev)

'''
3. Valid Parantheses
'''

s="{[()]}"

stack=[]

valid=True

for ch in s:
    if ch in '{[(':
        stack.append(ch)
    else:
        if not stack or stack.pop()!=mapping[ch]:
            valid=False
            break
print(valid)


'''
4. Count elements in stack without using len()
'''

stack=[1,2,3,4,5]

count=0

for _ in stack:
    count=count+1

print(count)
