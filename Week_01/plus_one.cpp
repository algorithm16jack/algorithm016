class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        vector<int> res = digits;
        vector<int>::iterator it = res.begin();
        int add_flag = 0;
        int current_digit = 0;
        int total_num = res.size();

        if (total_num == 1 && res[0] == 0) {
            res[0] = 1;
        }
        else {
            for (int i = 0; i < total_num; i++) {
                current_digit = res[total_num - 1 - i];
                if (i == 0) {
                    current_digit += 1;
                }
                else {
                    current_digit += add_flag;
                }
                
                if (current_digit == 10) {
                    add_flag = 1;
                    res[total_num - 1 - i] = 0;
                }
                else {
                    add_flag = 0;
                    res[total_num - 1 - i] = current_digit;
                }
                if (add_flag == 0) {
                    break;
                }
            }

            if (add_flag == 1) {
                res.insert(it, 1);
            }
        }

        return res;

    }
};
