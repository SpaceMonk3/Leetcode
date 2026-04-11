# brute force approach: nested loop and go thru each line with every other line, while calculating & comparing the area 
# and finding the largest one
#
# optimal approach: use a 2 pointer approach from either side of the array. ONLY MOVE THE pointer which has the 
# LOWEST HEIGHT inward. stop moving pointers when they both meet.
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        area = 0

        while(left != right):
            lineHeight = min(height[left], height[right])

            if (lineHeight * (right-left)) > area:
                area = lineHeight * (right-left)
            
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        
        return area