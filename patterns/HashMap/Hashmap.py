"""
Question 1 — Two Sum (unsorted)

Problem
Return indices of two numbers that sum to target.

nums = [2,7,11,15], target=9 → [0,1]
"""

def two_sum(nums, target):
    seen={}

    for i , num in enumerate(nums):
        diff=target-num

        if diff in see:
            return [seen[diff],i]

        seen[diff]=i



"""
Question 2 — Count frequencies of elements

Problem
Return frequency of each number.

[1,1,2,3,3,3] → {1:2, 2:1, 3:3}
"""

def count_all(nums):
    freq={}

    for num in nums:
        freq[num]=freq.get(num,0)+1

    return freq


"""
Question 3 — Find duplicates in array

Problem
Return all numbers that appear more than once.

[1,2,3,1,3,6,6] → [1,3,6]
"""

def duplicate(nums):
    real=set()
    duplicate=set()

    for num in nums:
        if num in real:
            duplicate.add(num)
        else:
            real.add(num)


    return list(duplicate)


"""
Question 4 — Longest consecutive sequence

Problem
Find length of longest consecutive numbers.

[100,4,200,1,3,2] → 4
(sequence: 1,2,3,4)
"""


def longest_sub(nums):
    num_set=set(nums)
    longest=0


    for num in num_set:
        if num-1 not in num_set:
            length=1
            while num+length in num_set:
                length=length+1
            longest=max(longest,length)

    return longest
