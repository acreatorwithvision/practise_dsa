'''
1. Reverse a string

Reverse the given string.
'''
s="python"
rev=""

for ch in s:
    rev=ch+rev

print(rev)


'''
2. Check if palindrome or not
'''

s1="madam"
s2=""
for ch in s1:
    s2=ch+s2

if s1==s2:
    print(True)
else:
    print(False)


'''
3. Check if vowel or not
'''

a="suhas"
vowels=set('aeiou')
count=0

for ch in s:
    if ch in vowels:
        count=count+1

print(count)

'''
4. First Non-repeating character.
'''

s="python"
freq={}

for ch in s:
    freq[q]=freq.get(ch,0)+1

for ch in s:
    if freq[ch]==1:
        print(ch)
        break
