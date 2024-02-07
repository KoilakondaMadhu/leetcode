#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

class Solution {
public:
    // Function to sort characters in a string based on their frequency
    string frequencySort(string s) {
        // Vector of pairs to store character frequencies
        vector<pair<int,char>> v;
        // Map to store character frequencies
        map<char,int> mp;

        // Count frequencies of each character in the input string
        for(int i = 0; i < s.size(); i++) {
            mp[s[i]]++;
        }

        // Convert the map to a vector of pairs (frequency, character)
        for(auto i : mp) {
            v.push_back({i.second, i.first});
        }

        // Sort the vector in decreasing order based on frequency
        sort(v.rbegin(), v.rend());

        // Construct the resulting string by appending characters in sorted order
        string ans;
        for(auto i : v) {
            // Append each character 'i.second' 'i.first' times
            for(int j = 0; j < i.first; j++) {
                ans += i.second;
            }
        }
        return ans; // Return the sorted string
    }
};

int main() {
    Solution sol;
    string input = "tree";
    string sorted = sol.frequencySort(input);
    cout << "Sorted string: " << sorted << endl;
    return 0;
}
