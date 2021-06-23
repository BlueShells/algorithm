class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        i = len(digits) -1 
        jin = 0 
        while i >= 0 :
            tmp = digits[i] + 1 
            if tmp  == 10 :
                
                digits[i] = 0 
                i = i - 1 
                print(digits)
            else:
                digits[i] = tmp
                break 
        if digits[0] == 0 :
            digits.insert(0,1)
        return digits
