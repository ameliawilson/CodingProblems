/* Problem 485
* Given a binary array, find the maximum number of consecutive 1s in this array.
* Input: [1,1,0,1,1,1]
* Output: 3 
*/

class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int max = 0;
        int count = 0;
        
        for (int n : nums)
        {
            if (n)
            {
                count++;
                if(count > max)
                {
                    max = count;
                }
            }
            else
                count = 0;
        }
        return max;
    }
};
