class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        i = 1
        mark = nums[0]
        while i < len(nums):
            if i > len(nums) - 1:
                return i
            if nums[i] == mark:
                nums.pop(i)
            else:
                mark = nums[i]
                i += 1
                if i == len(nums):
                    return i

        #return i

if __name__ == "__main__":
    mySolution = Solution()
    myNums = [0,0,1,1,1,2,2,3,3,4]
    result = mySolution.removeDuplicates(myNums)
    for i in range(result):
        print(i)