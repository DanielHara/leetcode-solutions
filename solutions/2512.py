"""
Question 2512: https://leetcode.com/problems/reward-top-k-students/

    Quite easy question, just do it
"""

from functools import cmp_to_key

class Solution:
    def sort_student_rewards(self, student_reward1, student_reward2):
        if student_reward1[1] > student_reward2[1]:
            return -1
        if student_reward1[1] < student_reward2[1]:
            return 1
        
        if student_reward1[0] < student_reward2[0]:
            return -1
        
        if student_reward1[0] > student_reward2[0]:
            return 1
        
        return 0


    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        reports = report
        student_ids = student_id

        positive_feedback_word_set = set()
        for word in positive_feedback:
            positive_feedback_word_set.add(word)

        negative_feedback_word_set = set()
        for word in negative_feedback:
            negative_feedback_word_set.add(word)
        
        student_reward_map = {}
        for report_index in range(len(reports)):
            student_id = student_ids[report_index]

            report = reports[report_index]

            words = report.split(' ')

            reward = 0
            for word in words:
                if word in positive_feedback_word_set:
                    reward = reward + 3
                elif word in negative_feedback_word_set:
                    reward = reward - 1
            
            student_reward_map[student_id] = reward

        student_reward_array = list(student_reward_map.items())

        student_reward_array.sort(key=cmp_to_key(self.sort_student_rewards))

        return map(lambda student_reward: student_reward[0], student_reward_array[0:k])

