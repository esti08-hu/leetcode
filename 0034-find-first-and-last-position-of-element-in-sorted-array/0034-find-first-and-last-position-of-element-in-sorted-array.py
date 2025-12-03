class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def firstOccerence(nums, target):
            low, high = 0, len(nums)-1
            res = -1
            while low <= high:
                mid = (low+high)//2

                if nums[mid] > target:
                    high = mid-1
                elif nums[mid] < target:
                    low = mid+1
                else:
                    res = mid
                    high = mid-1

            return res 
        
        def lastOccerence(nums, target):
            low, high = 0, len(nums)-1

            res =-1

            while low <= high:
                mid = (low+high)//2
                if nums[mid] < target:
                    low = mid +1
                elif nums[mid] > target:
                    high = mid - 1
                else:
                    res = mid
                    low = mid + 1

            return res 
        

        return [firstOccerence(nums, target), lastOccerence(nums, target)]
                