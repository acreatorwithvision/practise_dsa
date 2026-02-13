"""
Question 1 — Implement Queue

Problem
Make your own queue with push/pop.
"""
from collections import deque

class Queue:
    def __init__(self):
        self.q=deque()

    def push(self,x):
        self.q.append(x)
    def pop(self):
        self.q.popleft()

    def peek(self):
       return self.q[0]

    def empty(self):
        return len(q)==0


"""
Q2 — Print elements in queue
Problem

Print and empty queue.
"""

from collections import deque

q=deque([1,2,3,4,5])

while q:
    print(q.popleft())


"""
Q3 — Generate numbers from 1 to N
Problem

Print 1 to N using queue.
"""


from collections import deque

def generate_numbers(n):

    q=deque(range(1,n+1))


    while q:
        print(q.popleft())

"""
Reverse first K elements of queue
Problem

Queue = [1,2,3,4,5]
k=3
Result → [3,2,1,4,5]
"""

from collections import deque

def reversed_number(q,k):
    stack=[]

    for _ in range(k):
        stack.append(q.popleft())

    while stack:
        q.appendleft(stack.pop())

    return q
