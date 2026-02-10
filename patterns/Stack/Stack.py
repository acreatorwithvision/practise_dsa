"""
Question 1 — Valid Parentheses

Problem
Return True if brackets are valid.
"""

s='{([])}'

def parantheses(s):
    stack=[]
    pairs={')':'(',']':'[':'}':'{'}

    for ch in s:
        if ch in '{([':
            stack.append(ch)
        else:
            if not stack or stack.pop()!=pairs[ch]:
                return False
                break
    return len(stack)==0


"""
Question 2 — Remove Adjacent Duplicates

Problem

"abbaca" → "ca"
"""

s="abbaca"

def remove_ad(s):
    stack=[]

    for ch in s:
        if stack and stack[-1]==ch:
            stack.pop()

        else:
            stack.append(ch)
    return "".join(stack)


"""
Question 3 — Implement Stack using list

Problem
Create push, pop, top, empty.
"""

class Stack:
    def __init__(self):
        self.data=[]

    def push(self,x):
        self.data.append(x)
    def pop(self):
        return self.data.pop()
    def top():
        return self.data[-1]
    def empty():
        return len(self.data)==0

"""
Question 4 — Min Stack

Problem
Stack that returns minimum in O(1).
"""

class MinStack:
    def __init__(self):
        self.stack=[]
        self.min_stack=[]

    def push(self,val):
        self.stack.append(val)

        if not self.min_stack or val<=self.min_stack[-1]:
            self.min_stack.append(val)
    def pop(self):
        if self.stack[-1]==self.min_stack[-1]:
            self.min_stack.pop()
        self.stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin():
        return self.min_stack[-1]

