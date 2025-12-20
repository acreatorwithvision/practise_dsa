'''
1. Frequency of elements
 Count the number of elements in the array
'''

arr=[1,2,2,3,3,3]

freq={}

for ch in arr:
    freq[ch]=freq.get(ch,0)+1

for ch,count in freq.items():
    print(f"{ch}:{count}")

'''
2. Character with maximum frequency
'''

s="bananana"

freq={}

for ch in s:
    freq[ch]=freq.get(ch,0)+1

max_count=0
max_char=""

for ch,count in freq.items():
    if count>max_count:
        max_count=count
        max_char=ch

print(max_char)


'''
3. Check Anagram
'''

s1="silent"
s2="listen"

if len(s1)!=len(s2):
    print(False)

else:
    freq={}

    for ch in s1:
        freq[ch]=freq.get(ch,0)+1

    for ch in s2:
        if ch not in freq or freq[ch]==0:
            print(False)
            break

        freq[ch]=freq[ch]-1

    else:
        print(True)

'''
4. Majority Elements
'''

arr=[2,2,1,2,3,2,2]

freq={}

for ch in arr:
    freq[ch]=freq.get(ch,0)+1

n=len(arr)
for num,count in freq.items():
    if count>n//2:
        print(num)
        break
