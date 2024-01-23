# Question 2288: https://leetcode.com/problems/apply-discount-to-prices/

"""
    Just do it
"""

class Solution:
    def is_price(self, token: str) -> bool:
        if token[0] != '$' or len(token) <= 1:
            return False

        for i in range(1, len(token)):
            if not token[i].isdigit():
                return False

        return True


    def discountPrices(self, sentence: str, discount: int) -> str:
        tokens = sentence.split(' ')

        final_tokens = []
        for token in tokens:
            if self.is_price(token):
                price = int(token[1:])

                discounted = "$%.2f" % (price * (100 - discount) / 100)

                final_tokens.append(discounted)
            else:
                final_tokens.append(token)
        
        return ' '.join(final_tokens)
