import sys
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
    
        if len(nums2) < len(nums1):
            return self.findMedianSortedArrays(nums2, nums1)
        
        n1 = len(nums1)
        n2 = len(nums2)
        
        l = 0
        h = n1
        
        while(l <= h):
            
            cut1 = l + (h - l)/2
            cut2 = (n1 + n2) / 2 - cut1
            
            # l1
            if(cut1 == 0):
                l1 = -sys.maxsize - 1
            else:
                l1 = nums1[cut1 - 1]
                
            # l2
            if(cut2 == 0):
                l2 = -sys.maxsize - 1
            else:
                l2 = nums2[cut2 - 1] 
                
            # r1
            if(cut1 == n1):
                r1 = sys.maxsize
            else:
                r1 = nums1[cut1]
                
            # r2
            if(cut2 == n2):
                r2 = sys.maxsize
            else:
                r2 = nums2[cut2]
             
            if(l1 > r2):
                h = cut1 - 1
            elif(l2 > r1):
                l = cut1 + 1
                
            # Med found
            else:
                # Even
                if((n1+n2) % 2 == 0):
                    med = float(max(l1 , l2) + min(r1 , r2)) / 2
                    return med
                else:
                    return float(min(r1 , r2))
                
        
        
       