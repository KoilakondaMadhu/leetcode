class Solution(object):
    def canJump(self, nums):
  
        goal = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):  # checking from the back
            if i + nums[i] >= goal:
                print(f"i = {i} + nums[{i}] = {i + nums[i]} >= goal ({goal})")
                print(f"i: {i}, nums[{i}]: {nums[i]}")
                goal = i
                print(f"New goal: {goal}")
        return goal == 0

# Test cases
nums1 = [2, 3, 1, 1, 4]

sol = Solution()
print(sol.canJump(nums1))  # Expected output: True

i = 4 + nums[4] = 8 >= goal (4)
i: 4, nums[4]: 4
New goal: 4
i = 3 + nums[3] = 4 >= goal (4)
i: 3, nums[3]: 1
New goal: 3
i = 2 + nums[2] = 3 >= goal (3)
i: 2, nums[2]: 1
New goal: 2
i = 1 + nums[1] = 4 >= goal (2)
i: 1, nums[1]: 3
New goal: 1
i = 0 + nums[0] = 2 >= goal (1)
i: 0, nums[0]: 2
New goal: 0
True

=== Code Execution Successful ===
