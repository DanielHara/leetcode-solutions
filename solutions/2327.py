# Question 2327: https://leetcode.com/problems/number-of-people-aware-of-a-secret/

"""
    This question is super interesting! Just keep two dicts, one to keep a count of how many people start telling the secret on a certain day,
    and another to count how many people forget the secret on a certain day.
"""

class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        day_to_number_people_who_will_forget_secret = {}
        day_to_number_people_who_start_telling_secret = {}

        number_people_who_know_the_secret = 1
        number_people_who_tell_the_secret = 0
        day_to_number_people_who_start_telling_secret[delay + 1] = 1
        day_to_number_people_who_will_forget_secret[forget + 1] = 1

        for day in range(2, n + 1):
            number_people_who_tell_the_secret = number_people_who_tell_the_secret + day_to_number_people_who_start_telling_secret.get(day, 0) - day_to_number_people_who_will_forget_secret.get(day, 0)

            day_to_number_people_who_start_telling_secret[delay + day] = day_to_number_people_who_start_telling_secret.get(delay + day, 0) + number_people_who_tell_the_secret
            day_to_number_people_who_will_forget_secret[forget + day] = day_to_number_people_who_will_forget_secret.get(forget + day, 0) + number_people_who_tell_the_secret
            
            number_people_who_know_the_secret = number_people_who_know_the_secret + number_people_who_tell_the_secret - day_to_number_people_who_will_forget_secret.get(day, 0)
        
        mod = 10**9 + 7
        return number_people_who_know_the_secret % mod
