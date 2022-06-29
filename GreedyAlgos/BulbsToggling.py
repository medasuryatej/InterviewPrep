"""
Given an initial array of bulbs (1-indicates Turned On, 0-indicates Turned Off). Toggling a bulb at ith index, flips the value of every other bulb on its right.
Determine the minimum number of flips required.

Ex: 
Input:
[1,0,1]

Output:
2
"""

class Solution:
  def bulbs(self, A):
    cost = 0
    for b in A:
      if cost % 2 == 0:
        # bulb doesn't change value
        b = b
      else:
        # bulb value flips
        b = not b
      
      # check if b is 0
      if not b:
        cost += 1
      else:
        continue
  return cost
