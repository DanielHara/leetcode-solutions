/*
    One way to do this is using a multiset

    The thing with a multiset is that, although is supports finding the first element < threshold in O(log N) time,
    it still doesn't support counting how many elements are < threshold efficiently.
    That's why you have to use a ordered_multiset trick which was suggested to me by ChatGPT, LOL
    In general, multisets are very useful data structures, which support searching, inserting, and finding the first element < threshold,
    all in O(log N) time
*/

#include <stdint.h>
#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>

using namespace std;
using namespace __gnu_pbds;

// Ordered multiset (supports duplicates via pair trick)
template<typename T>
using ordered_multiset = tree<
    pair<T,int>,                // store (value, unique_id) so duplicates allowed
    null_type,
    less<pair<T,int>>, 
    rb_tree_tag,
    tree_order_statistics_node_update>;

class Solution {
public:
    int countRangeSum(vector<int>& nums, int lower, int upper) {
        ordered_multiset<int64_t> ms;
        int result = 0;

        // Insert elements (attach unique counter to handle duplicates)
        int id = 0;

        ms.insert({ 0, id++ });

        // Save the prefix sums in the multiset
        int64_t s = 0;
        for (int end = 0; end < nums.size(); end++) {
            s = s + nums[end];

            /*
                Now, find the amount of elements in the multiset which range
                between [s - upper, s - lower]

                That is, the amount of elements that are < s - lower + 1, substracted
                by the amount of elements which are < s - upper
            */

            int count = ms.order_of_key({s - lower + 1, 0}) - ms.order_of_key({s - upper, 0});
            result = result + count;

            ms.insert({ s, id++ });
        }

        return result;
    }
};
