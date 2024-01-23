# Question 2271: https://leetcode.com/problems/maximum-white-tiles-covered-by-a-carpet/

"""
    A bit of DP and binary search does the trick
"""

class Solution:
    # Returns the largest index for which tiles[i][0] <= target
    def binarySearch(self, tiles: List[List[int]], i: int, j: int, target):
        if i > j:
            return None
        
        half = (i + j) // 2

        if tiles[half][0] <= target and (half == j or tiles[half + 1][0] > target):
            return half
        if tiles[half][0] <= target:
            return self.binarySearch(tiles, half + 1, j, target)
        return self.binarySearch(tiles, i, half - 1, target)

    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        tiles.sort(key=lambda tile: tile[0])

        S = []
        for tile in tiles:
            S.append(tile[1] - tile[0] + 1 + (S[-1] if S else 0))

        result = 0
        for index_tile, tile in enumerate(tiles):
            target = tile[0] + carpetLen - 1
            last_tile_index = self.binarySearch(tiles, 0, len(tiles) - 1, target)

            candidate = None

            if last_tile_index > index_tile:
                candidate = (S[last_tile_index - 1] if last_tile_index > 0 else 0) - (S[index_tile - 1] if index_tile > 0 else 0) + min(target - tiles[last_tile_index][0] + 1, tiles[last_tile_index][1] - tiles[last_tile_index][0] + 1)
            else:
                candidate = min(carpetLen, tile[1] - tile[0] + 1)
            result = max(result, candidate)

        return result
