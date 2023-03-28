# Question 1797: https://leetcode.com/problems/design-authentication-manager/

"""
Just do it. Very interesting well described and posed question.
"""

class AuthenticationManager:
    def __init__(self, timeToLive: int):
        self.timeToLive = timeToLive
        self.token_to_expiration_time_map = {}

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.token_to_expiration_time_map[tokenId] = currentTime + self.timeToLive

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.token_to_expiration_time_map:
            if self.token_to_expiration_time_map[tokenId] > currentTime:
                self.token_to_expiration_time_map[tokenId] = currentTime + self.timeToLive
            else:
                del self.token_to_expiration_time_map[tokenId]

    def countUnexpiredTokens(self, currentTime: int) -> int:
        keys = list(self.token_to_expiration_time_map.keys())

        result = 0
        for key in keys:
            if self.token_to_expiration_time_map[key] <= currentTime:
                del self.token_to_expiration_time_map[key]
            else:
                result = result + 1

        return result
