# Question 929: https://leetcode.com/problems/unique-email-addresses/description/

"""
Trivial question, just do it!
"""

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        email_set = set()

        for email in emails:
            [local_name, domain_name] = email.split('@')

            local_name = local_name.split('+')[0]
            local_name = ''.join(local_name.split('.'))

            email_set.add(local_name + '@' + domain_name)
        
        return len(email_set)
