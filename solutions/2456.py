"""
    Question 2456: https://leetcode.com/problems/most-popular-video-creator/description/

    Just use some hashmaps, nothing fancy. Just do it.
"""

class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        creator_to_popularity = {}

        creators_to_video_record = {}
        for index in range(len(creators)):
            creator = creators[index]
            video_id = ids[index]
            view = views[index]

            if creator not in creators_to_video_record:
                creators_to_video_record[creator] = {}

            creators_to_video_record[creator][video_id] = creators_to_video_record[creator].get(video_id, 0) + view
            creator_to_popularity[creator] = creator_to_popularity.get(creator, 0) + view

        highest_popularity = max(creator_to_popularity.values())

        result = []
        for creator in creators_to_video_record:
            if creator_to_popularity[creator] != highest_popularity:
                continue

            video_records = creators_to_video_record[creator].items()
            highest_views = max(creators_to_video_record[creator].values())

            most_popular_video_id = None
            for [video_id, number_views] in video_records:
                if number_views == highest_views:
                    if most_popular_video_id is None or video_id < most_popular_video_id:
                        most_popular_video_id = video_id

            result.append([creator, most_popular_video_id])

        return result
