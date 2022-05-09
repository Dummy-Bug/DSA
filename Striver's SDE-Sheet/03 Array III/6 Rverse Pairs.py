# https://leetcode.com/problems/reverse-pairs/
class Solution:
    
    def __init__(self):
        from sys import stdin,setrecursionlimit
        setrecursionlimit(10**7)
        
    def reversePairs(self, nums: List[int]) -> int:
        
        inversions = self.mergeSort(nums,0,len(nums)-1)
        return inversions
    
    
    def merge(self,arr, left, mid, right):

        invCount = 0
        temp = [0 for x in range(right - left + 1)]
        
        j = mid + 1
        
        for i in range(left,mid+1):
            
            while j<= right and arr[i] > 2*arr[j]:
                j = j + 1
            invCount += j - (mid + 1) 
        
        # Function to merge the two subarrays.
        
        i = left
        j = mid + 1
        k = 0
        
        while ((i <= mid) and (j <= right)):
            if (arr[i] <= arr[j]):
                temp[k] = arr[i]
                k += 1
                i += 1

            else:
                temp[k] = arr[j]
                k += 1
                j += 1

        while (i <= mid):
            temp[k] = arr[i]
            k += 1
            i += 1

        while (j <= right):
            temp[k] = arr[j]
            k += 1
            j += 1

        k = 0
        for i in range(left, right + 1):
            arr[i] = temp[k]
            k += 1

        return invCount

    # Function to split two subarrays and then merge them and count inversions.
    def mergeSort(self,arr, left, right):
        invCount = 0

        if (right > left):
            mid = (right + left) // 2

            invCount = self.mergeSort(arr, left, mid)
            invCount += self.mergeSort(arr, mid + 1, right)

            # Merge both parts and count their combined inversions.
            invCount += self.merge(arr, left, mid, right)

        return invCount