"""
1679. Max Number of K-Sum Pairs

https://leetcode.com/problems/max-number-of-k-sum-pairs/description/?envType=study-plan-v2&envId=leetcode-75

Max number of operations we can do on the array
Find pairs and remove until we cant do any more

Naive:
Iterate over the list continounsly trying to find a pair for each value x.
Remove when we find a match
Continnue until no more matches

O(n^2) runtime

Optmize:
Sort the list nlogn
Scan the array with a left and right pointer

if a[l]+a[r] == k
    counter += 1
    l+=1
    r-=1
if a[l]+a[r] >k:
    r-=1
else:
    l+=1

O(nlogn) Runtime

Test

[1,2,3,4]

l r count
0 3   0
1 2   1
2 2   1

[1,3,3,3,4]  k = 6
l r count
0 4   0
1 3   1
2 2    1

Another Approach:
Create a dict counter

Two Pass
Iterate over each key, check dict[k-key] if it is greater than 0 then we take the min and add that to the total
Edge case where k-key = key, in this case take floor(dict[k]/2) and add that to the total

Single PAss
Go left to right
Check if k-A[i] in dict, if so then update our total and dcrement k-A[-1] and continue
Else we add/increment A[i]


"""

from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        r = len(nums) - 1
        matches = 0

        while l < r:
            if nums[l] + nums[r] == k:
                matches += 1
                l += 1
                r -= 1
            elif nums[l] + nums[r] > k:
                r -= 1
            else:
                l += 1

        return matches
