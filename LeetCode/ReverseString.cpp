/**  #344. Reverse String */
class Solution {
public:
    string reverseString(string s) {
        int len = s.size() - 1;
        string reverse;
        for (int i = len; i >= 0; i--){
            reverse += s[i];
        }
        return reverse;
    }
};
