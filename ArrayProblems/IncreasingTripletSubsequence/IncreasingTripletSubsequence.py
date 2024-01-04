"""
334. Increasing Triplet Subsequence
https://leetcode.com/problems/increasing-triplet-subsequence/

        Need to find a triplet such that i<j<k and a[i] < a[j] < a[k]

        [1,2,3,4,5]
        in this case i,j,k has mulitple solutions

        [5,4,3,2,1]
        no possible combination

        [2,1,5,0,4,6]
        0,4,6 works

        Brute Force
        We initialize 3 points, i,j,k
        for i in range(N):
            for j in range(i+1,N):
                for k in range(j+1,N):
                    if nums[i] < nums[j] < nums[k]:
                        return True

        return False

        O(1) Space
        O(n^3) time as we have three points we are iterating -> this causes TLE


        Speed Up:
        We can skip testing duplicates that are next to each other.
        This will avoid double computing possible triplet
        N = len(nums)
        i = 0
        j = 1
        k = 2
        while i<N-2:
            while nums[i] == nums[i+1] and i<N-2:
                i+=1
            for j in range(i+1,N):
                if j<N-1 and nums[j] == nums[j+1]:
                    continue
                for k in range(j+1,N):
                    if nums[i] < nums[j] < nums[k]:
                        return True
            i+=1

        return False


        This will still give us a TLE

        Speed up 2:
        We can store local mins from left to right
        We store local maxs from right to left

        then iterate over nums

        if loc_min<nums[i]<loc_max[i]:
            return True

        return False
        O(n) memory
        O(n) Runtime

        N = len(nums)
        loc_mins = []
        loc_maxs = []

        lmin = nums[0]
        for x in nums[1:]:
            loc_mins.append(lmin)
            lmin= min(x,lmin)
        #print(loc_mins)

        lmax = nums[-1]
        for idx in range(N-2,-1,-1):
            x = nums[idx]
            loc_maxs.insert(0,lmax)
            lmax = max(x,lmax)
        #print(loc_maxs)

        for j in range(1,N):
            #We can speed this up by skipping duplicates
            if nums[j] == nums[j-1]:
                continue
            if loc_mins[j-1] < nums[j] < loc_maxs[j-1]:
                return True


        return False

        Speed Up 3:
        We can store the current min and second_min
        We update min if we find A[i] less than it
        We update second min if we find a value > min but less than s_min
        We return True if the value is bigger than both as this implies we have a comination in our list somewhere
        The TRICK here is that we dont need to find a valid sequnce, just return True/False. So we only care about proving the existance rather than acutally findingit
            [7,1,2,0,3]
        min  7 1 1 0 True
        smin - - 2 2 True
        We return true on the last element asit is bigger than both
            [7,1,2,0,-1]
        min  7 1 1 0 -1  FALSE
        smin - - 2 2  2
        We return false as we reached end

        if A[i] <= min:
            min = A[i]
        elif A[i] <= smin:
            smin = A[i]
        else:
            return True

        return False

        O(n) rumtime O(1) space
"""
from typing import List


class Solution:


    def increasingTriplet(self, nums: List[int]) -> bool:
        lmin = float("inf")
        smin = float("inf")

        for i in range(len(nums)):
            if nums[i] <= lmin:
                lmin = nums[i]
            elif nums[i] <= smin:
                smin = nums[i]
            else:
                return True
        return False

