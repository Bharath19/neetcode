class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(arr, L, M, R):
            left, right = arr[L:M+1], arr[M+1:R+1]
            arrp, lp, rp = L, 0, 0

            while lp < len(left) and rp < len(right):
                if left[lp] <= right[rp]:
                    arr[arrp] = left[lp]
                    lp += 1
                    arrp += 1
                else:
                    arr[arrp] = right[rp]
                    rp += 1
                    arrp += 1
            while lp < len(left):
                arr[arrp] = left[lp]
                lp += 1
                arrp += 1
            while rp < len(right):
                arr[arrp] = right[rp]
                rp += 1
                arrp += 1
            return arr


        def mergeSort(arr, l, r):
            if l == r:
                return arr
            
            m = ( l + r ) // 2
            mergeSort(arr, l, m)
            mergeSort(arr, m+1, r)

            return merge(arr, l, m, r)
        
        return mergeSort(nums, 0, len(nums))
