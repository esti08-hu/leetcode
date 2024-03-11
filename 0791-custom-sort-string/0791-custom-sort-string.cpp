class Solution {
public:
    string customSortString(string order, string s) {
        vector<int> freq(26, 0); 
        
        for (char ch : s) {
            freq[ch - 'a']++;
        }

        string result;

        
        for (char ch : order) {
            while (freq[ch - 'a'] > 0) {
                result.push_back(ch);
                freq[ch - 'a']--;
            }
        }

   
        for (int i = 0; i < 26; i++) {
            while (freq[i] > 0) {
                result.push_back('a' + i);
                freq[i]--;
            }
        }

        return result;
    }
};