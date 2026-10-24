class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        longest_sequence = 0
        for n in range(len(nums)):
            if nums[n] - 1 not in numsSet:
                length = 0
                while(nums[n] + length) in numsSet:
                    length += 1
                    longest_sequence = max(length, longest_sequence)
        return longest_sequence