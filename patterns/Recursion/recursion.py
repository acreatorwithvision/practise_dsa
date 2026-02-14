"""
Q1 — Print numbers from N to 1
Problem

Print 5 to 1.
"""

def print_down(n):
    if n==0:
        return None
    print(n)
    print_down(n-1)


"""
Q2 — Print 1 to N
"""

def print_up(n):
    if n==0:
        return
    print(n-1)
    print(n)

"""
Sum of numbers 1 to N
Problem

Find sum till N.
"""

def sum_n(n):
    if n==0:
        return O
    return n+sum_n(n-1)


