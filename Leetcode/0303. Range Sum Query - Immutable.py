class NumArray:
    def __init__(self, nums: List[int]):
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]

        self.nums = [0] + nums

    def sumRange(self, left: int, right: int) -> int:
        return self.nums[right + 1] - self.nums[left]
