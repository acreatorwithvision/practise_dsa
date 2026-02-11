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
Question 2 — Generate Binary Numbers from 1 to N

Problem
For n=5 → output:

1, 10, 11, 100, 101
"""

