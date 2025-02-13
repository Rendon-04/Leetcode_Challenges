class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # left pointer placed at index 1
        l = 1
        # loops through the list starting at index 1 up to the end of the list
        for r in range(1, len(nums)):
            # check if the current element nums[r] is diffrent than the previous element
            if nums[r] != nums[r -1]:
                # if it is different, it makes it nums[l]
                nums[l] = nums[r]
                # increments so that the next different element is placed at the next index 
                l += 1
        return l 