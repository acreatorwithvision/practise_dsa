'''
1. Reverse a string
In this problem we should reverse a string without slicing.
'''

s="suhas"
r=""

for i in s:
    r=i+r

print(r)


'''
2. Check if it is palindrome
Here we need to check if it is palindrome string or not.
'''

s="madam"
r=s[::-s]

is_pal=False

if s==r:
    is_pal=True
    print(is_pal)
else:
    print(is_pal)
