

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))

# Example usage
nums = [1, 2, 3, 4, 1]
solution = Solution()
print(solution.containsDuplicate(nums))  # Output: True
