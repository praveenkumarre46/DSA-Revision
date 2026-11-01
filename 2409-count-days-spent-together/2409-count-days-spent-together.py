class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        def date_to_day(date_str: str) -> int:
            month, day = map(int, date_str.split('-'))
            return sum(days[:month - 1]) + day
        
        start_alice = date_to_day(arriveAlice)
        end_alice = date_to_day(leaveAlice)
        start_bob = date_to_day(arriveBob)
        end_bob = date_to_day(leaveBob)
        
        overlap_start = max(start_alice, start_bob)
        overlap_end = min(end_alice, end_bob)
        
        return max(0, overlap_end - overlap_start + 1)