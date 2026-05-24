class Solution:
    def merge(self, left: List[int], right: List[int]) -> List[int]:
        res = []

        left_pos, right_pos = 0, 0
        while left_pos < len(left) and right_pos < len(right):
            if left[left_pos] > right[right_pos]:
                res.append(right[right_pos])
                right_pos += 1
            else:
                res.append(left[left_pos])
                left_pos += 1

        if left_pos < len(left):
            res.extend(left[left_pos:])
        if right_pos < len(right):
            res.extend(right[right_pos:])

        return res

    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        left_sort = self.sortArray(nums[:len(nums)//2])
        right_sort = self.sortArray(nums[len(nums)//2:])

        return self.merge(left_sort, right_sort)