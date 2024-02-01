class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()  # Sort the array to simplify the process
        n = len(nums)
        result = []

        # Helper function to check if an array of size 3 can be formed with given constraints
        def check(arr):
            return arr[2] - arr[0] <= k

        # Iterate through the sorted array and form arrays of size 3
        for i in range(0, n, 3):
            # Check if remaining elements are enough to form an array of size 3
            if i + 2 < n and check([nums[i], nums[i+1], nums[i+2]]):
                result.append([nums[i], nums[i+1], nums[i+2]])
            else:
                return []  # It's not possible to form an array satisfying the conditions

        return result

# Test the solution
solution = Solution()
nums1 = [1, 3, 4, 8, 7, 9, 3, 5, 1]
k1 = 2
print(solution.divideArray(nums1, k1))  # Output: [[1, 1, 3], [3, 4, 5], [7, 8, 9]]

nums2 = [1, 3, 3, 2, 7, 3]
k2 = 3
print(solution.divideArray(nums2, k2))  # Output: []
