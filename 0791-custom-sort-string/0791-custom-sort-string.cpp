class Solution {
public:
    string customSortString(string order, string s) {
        unordered_map<char, int> freq; 
        for (char ch : s) {
            freq[ch]++;
        }

        string result;

        for (char ch : order) {
            if (freq.find(ch) != freq.end()) {
                result.append(freq[ch], ch);
                freq.erase(ch);
            }
        }

        for (auto it : freq) {
            result.append(it.second, it.first);
        }

        return result;
    }
};