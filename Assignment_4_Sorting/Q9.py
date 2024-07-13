from typing import List

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        rank = sorted(score, reverse=True)
        rank_dict = {v: str(i + 1) for i, v in enumerate(rank)}
        for i, r in enumerate(["Gold Medal", "Silver Medal", "Bronze Medal"]):
            if i < len(rank):
                rank_dict[rank[i]] = r
        return [rank_dict[s] for s in score]


sol = Solution()
score = [5, 4, 3, 2, 1]
print(sol.findRelativeRanks(score))  
