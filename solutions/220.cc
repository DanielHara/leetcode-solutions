// Question 220: https://leetcode.com/problems/contains-duplicate-iii/

/*
    Quite hard question, and the hints aren't very useful. The trick in this question is that you have to efficiently keep
    a sorted array, and be able to delete, search and insert an element to this sorted array, while still keeping it sorted.
    That's the purpose of a multiset in C++, which doesn't exist in Python out of the box. It implements a black-red tree (https://en.wikipedia.org/wiki/Red%E2%80%93black_tree),
    which allows us to perform each of those operations in O(log N) time, making the whole algorithm O(N log(N)) in time.
*/


class Solution {
public:
    bool containsNearbyAlmostDuplicate(vector<int>& nums, int indexDiff, int valueDiff) {
        multiset<int> ms_1 = {};
        multiset<int> ms_2 = {};
 
        int size = nums.size();
        
        for (int index = 0; index < size; index++) {
            if (index >= indexDiff + 1) {
                auto erase_iterator_1 = ms_1.find(nums[index - (indexDiff + 1)]);
                ms_1.erase(erase_iterator_1);

                auto erase_iterator_2 = ms_2.find(-1*nums[index - (indexDiff + 1)]);
                ms_2.erase(erase_iterator_2);
            }

            int num = nums[index];
            // Multiset is empty
            if (ms_1.size() == 0) {
                ms_1.insert(num);
                ms_2.insert(-1 * num);
            }
            // Case where ms_1.begin() <= num <= ms_1.rbegin()
            else if ( (*(ms_1.begin())) <= num && num <= (*(ms_1.rbegin()))) {
                auto first_element_not_less_than_num_it = ms_1.lower_bound(num);
                int first_element_not_less_than_num = *first_element_not_less_than_num_it;

                if (first_element_not_less_than_num - num <= valueDiff) {
                    return true;
                }

                auto first_negative_element_not_less_than_negative_num_it = ms_2.lower_bound(-1 * num);
                int first_negative_element_not_less_than_negative_num = * first_negative_element_not_less_than_negative_num_it;

                if (abs(-1*num - first_negative_element_not_less_than_negative_num) <= valueDiff) {
                    return true;
                }

                ms_1.insert(num);
                ms_2.insert(-1 * num);
            }
            // Case where num > ms_1.rbegin()
            else if (num > (*(ms_1.rbegin()))) {
                auto largest_element_it = ms_1.rbegin();
                int largest_element = *largest_element_it;

                if (abs(largest_element - num) <= valueDiff) {
                    return true;
                }

                ms_1.insert(num);
                ms_2.insert(-1 * num);
            }
            // Case where num < ms_1.begin()
            else {
                auto smallest_element_it = ms_1.begin();
                int smallest_element = *smallest_element_it;

                if (abs(smallest_element - num) <= valueDiff) {
                    return true;
                }

                ms_1.insert(num);
                ms_2.insert(-1 * num);
            }
        }

        return false;
    }
};
