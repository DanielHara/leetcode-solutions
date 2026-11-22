"""
Question 1348: https://leetcode.com/problems/tweet-counts-per-frequency/

    Good question to refresh how to use a multiset in C++
"""

class TweetCounts {
public:
    std::unordered_map<std::string, std::multiset<int>> tweetName2Multiset;

    TweetCounts() {
    }
    
    void recordTweet(string tweetName, int time) {
        if (tweetName2Multiset.count(tweetName) == 0) {
            std::multiset<int> timeMultiset;
            timeMultiset.insert(time);

            tweetName2Multiset.insert({ tweetName, timeMultiset});
        }
        else {
            tweetName2Multiset[tweetName].insert(time);
        }
    }
    
    vector<int> getTweetCountsPerFrequency(string freq, string tweetName, int startTime, int endTime) {
        vector<int> answer;

        std::multiset<int> timeMultiset = tweetName2Multiset.at(tweetName);

        while (startTime <= endTime) {
            auto lower_bound = timeMultiset.lower_bound(startTime);
            
            int endChunkTime = startTime;
            if (freq == "minute") {
                endChunkTime = min(endChunkTime + 60, endTime + 1);
            }
            else if (freq == "hour") {
                endChunkTime = min(endChunkTime + 60 * 60, endTime + 1);
            }
            else if (freq == "day") {
                endChunkTime = min(endChunkTime + 24 * 60 * 60, endTime + 1);
            }

            auto upper_bound = timeMultiset.lower_bound(endChunkTime);

            int count = std::distance(lower_bound, upper_bound);

            answer.push_back(count);

            if (freq == "minute") {
                startTime = startTime + 60;
            }
            else if (freq == "hour") {
                startTime = startTime + 60 * 60;
            }
            else if (freq == "day") {
                startTime = startTime + 24 * 60 * 60;
            }
        }

        return answer;
    }
};

/**
 * Your TweetCounts object will be instantiated and called as such:
 * TweetCounts* obj = new TweetCounts();
 * obj->recordTweet(tweetName,time);
 * vector<int> param_2 = obj->getTweetCountsPerFrequency(freq,tweetName,startTime,endTime);
 */
