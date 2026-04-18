class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # --------------------------------
        # Brute force
        # --------------------------------
        # for first_idx in range(len(nums)-1):
        #     for second_idx in range(first_idx+1, len(nums)):
        #         if nums[first_idx] + nums[second_idx] == target:
        #             return [first_idx, second_idx]

        # --------------------------------
        # Hashmap (2-pass)
        # --------------------------------
        # lookup = {}
        # for idx, value in enumerate(nums):
        #     lookup[value] = idx

        # for idx, value in enumerate(nums):
        #     if target - value in lookup:
        #         if idx == lookup[target-value]:
        #             continue
        #         return [idx, lookup[target-value]]

        # --------------------------------
        # Hashmap (1-pass)
        # --------------------------------
        lookup = {}
        for idx, value in enumerate(nums):
            complement = target - value

            if complement in lookup:
                return [lookup[complement], idx]
            lookup[value] = idx
