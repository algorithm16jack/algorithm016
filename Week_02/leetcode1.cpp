class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> res;
        unordered_map<int, int> dict;

        for (int i = 0; i < nums.size(); i++) {
            if (dict.count(target - nums[i]) == 1) {
                res.push_back(dict[target - nums[i]]);
                res.push_back(i); 
                break;              
            }
            else {
                dict[nums[i]] = i;
            }          
        }     

        return res;
    }
};