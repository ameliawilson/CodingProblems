#################################################################
# The input strings will not have extra blank.
# The input strings will be given in the form of a+bi, 
# where the integer a and b will both belong to the range of [-100, 100]. 
# And the output should be also in this form.
# [Problem 537]
#################################################################
class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a_ls = a.split("+")
        # a = w+xi
        w = int(a_ls[0])
        x = a_ls[1]
        x = int(x[:-1])

        # b = y+zi
        b_ls = b.split("+")
        y = int(b_ls[0])
        z = b_ls[1]
        z = int(z[:-1])

        A = (w*y) - (x*z)
        B = (w*z + x*y)
        
        return str(A) + "+" + str(B) + "i" 
