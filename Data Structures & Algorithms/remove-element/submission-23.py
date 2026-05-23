class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        swap_index = len(nums) - 1
        i = 0
        while i <= swap_index:
            if nums[i] == val:
                nums[i], nums[swap_index] = nums[swap_index], nums[i]
                swap_index -= 1
                if nums[i] != val:
                    i += 1
            else:
                i += 1
        return i