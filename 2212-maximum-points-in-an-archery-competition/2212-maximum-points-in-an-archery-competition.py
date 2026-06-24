class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        
        def rec(i, rem_arrows):
            if i == 12 or rem_arrows == 0:
                return 0, [0] * 12

            score1, dist1 = rec(i + 1, rem_arrows)

            score2, dist2 = -1, []
            arrows_needed = aliceArrows[i] + 1
            if rem_arrows >= arrows_needed:
                sub_score, sub_dist = rec(i + 1, rem_arrows - arrows_needed)
                score2 = i + sub_score
                dist2 = sub_dist[:]
                dist2[i] = arrows_needed

            if score2 > score1:
                return score2, dist2
            return score1, dist1

        max_score, final_dist = rec(0, numArrows)
        final_dist[0] += numArrows - sum(final_dist)
        return final_dist