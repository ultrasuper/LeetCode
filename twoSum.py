class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
#         length = len(nums)
#         nums.sort()
#         target_pos = length
#         for i in range(0, length):
#             if nums[i] > target:
#                 target_pos = i
#                 break

#         for i in range(0,target_pos):
#             for j in range(i+1,length):
#                 if nums[i] + nums[j] == target:
#                     return [i,j]

        
        orderbook = {}
        for i in range(0,len(nums)):
            if nums[i] in orderbook:
                orderbook[nums[i]].append(i)
            else:
                orderbook[nums[i]] = [i]
        for i in nums:
            if target-i in nums:
                if target-i != i:
                    return [orderbook[i][0],orderbook[target-i][0]]
                else:
                    if len(orderbook[i]) >= 2:
                        return orderbook[i][:2]