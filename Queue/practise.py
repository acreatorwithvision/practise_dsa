'''
1. Queue operations
'''

from collections import deque

q=deque()

q.append(10) #enque operation
q.append(20)
q.append(30)

print(q.popleft())

'''
2. Print Queue elements in FIFO order
'''

from collections import deque

q=deque([10,20,30])

for item in q:
    print(item,end=" ")


'''
3. Find first and last element
'''

from collections import deque

q=deque([10,20,30])

print("First: ",q[0])
print("Last: ",q[-1])


'''
4. Simulate ticket Queue
'''

from collections import deque

queue=[1,2,3,4]

q=deque(queue)

while q:
    print("Serving: ",q.popleft())



