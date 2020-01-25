from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
    	clost = nums[0] + nums[1] + nums[2]
    	nums = sorted(nums)
    	for i in range(len(nums)-2):
    		if i > 0 and nums[i] == nums[i-1]:
    			continue
    		l = i + 1
    		r = len(nums) - 1
    		while l < r:
    			if nums[i] + nums[l] + nums[r] - target == 0:
    				return target
    			if abs(nums[i] + nums[l] + nums[r] - target) < \
    			abs(clost - target):
    				clost = nums[i] + nums[l] + nums[r]
    			if nums[i] + nums[l] + nums[r] - target < 0:
    				while l < r and nums[l] == nums[l+1]:
    					l += 1
    				l += 1
    			else:
    				while l < r and nums[r] == nums[r-1]:
    					r -= 1
    				r -= 1
    	return clost

s = Solution()
print(s.threeSumClosest([13,2,0,-14,-20,19,8,-5,-13,-3,20,15,20,5,13,14,-17,-7,12,-6,0,20,-19,-1,-15,-2,8,-2,-9,13,0,-3,-18,-9,-9,-19,17,-14,-19,-4,-16,2,0,9,5,-7,-4,20,18,9,0,12,-1,10,-17,-11,16,-13,-14,-3,0,2,-18,2,8,20,-15,3,-13,-12,-2,-19,11,11,-10,1,1,-10,-2,12,0,17,-19,-7,8,-19,-17,5,-5,-10,8,0,-12,4,19,2,0,12,14,-9,15,7,0,-16,-5,16,-12,0,2,-16,14,18,12,13,5,0,5,6], -59))