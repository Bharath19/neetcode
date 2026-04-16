class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        1. Brute Force
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False
        """

        """
        2. Using Set
        """
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False




