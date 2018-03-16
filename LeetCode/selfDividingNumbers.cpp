/** Leet Code #728. Self Dividing Numbers
*
* A self-dividing number is a number that is divisible by every digit it contains.
* EX: 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
* Also, a self-dividing number is not allowed to contain the digit zero.
* Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.
*/
class Solution {
public:
    bool checkDigits(int x){
        int y=x;                
        while (x > 0 ){
            int temp = x%10; // isolate "ones" digit
            if (temp == 0 )
                return false; // digit is 0, not allowed
            if (y%temp!=0)
                return false; // orginal num is not divisible by its digit
            x=x/10; // remove "ones" digit
        }
        return true;
    }
    vector<int> selfDividingNumbers(int left, int right) {
        vector<int> nums;

        for (int i =left; i <= right; i++){
            if (checkDigits(i)) nums.push_back(i);
        }
        return nums;
    }
};
