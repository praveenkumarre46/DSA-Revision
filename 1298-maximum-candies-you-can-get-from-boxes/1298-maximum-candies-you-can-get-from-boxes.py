from collections import deque

class Solution:
    def maxCandies(self, status: list[int], candies: list[int], keys: list[list[int]], containedBoxes: list[list[int]], initialBoxes: list[int]) -> int:
        ownedkeys = set()
        visited = set()
        owned_boxes = set()
        queue = deque()

        for inbx in initialBoxes:
            owned_boxes.add(inbx)
            if status[inbx] == 1:
                queue.append(inbx)
                visited.add(inbx)

        maxcandies = 0
        
        while queue:
            node = queue.popleft()
            maxcandies += candies[node]
            
            for key in keys[node]:
                ownedkeys.add(key)
                if key in owned_boxes and key not in visited:
                    queue.append(key)
                    visited.add(key)
                
            for box in containedBoxes[node]:
                owned_boxes.add(box)
                if (status[box] == 1 or box in ownedkeys) and box not in visited:
                    queue.append(box)
                    visited.add(box)

        return maxcandies