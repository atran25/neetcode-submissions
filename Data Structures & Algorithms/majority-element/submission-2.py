class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cur_candidate = None
        count = 1

        for num in nums:
            if cur_candidate != num:
                count -= 1
            else:
                count += 1
            if count == 0:
                cur_candidate = num
                count += 1
        return cur_candidate