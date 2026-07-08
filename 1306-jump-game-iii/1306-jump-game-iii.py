class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        queue=deque([start])
        visited=set()
        visited.add(start)
        while queue:
            ind=queue.popleft()
            if arr[ind]==0:
                return True
            if ind-arr[ind]>=0 and ind-arr[ind] not in visited :
                visited.add(ind-arr[ind])
                queue.append(ind-arr[ind])
            if ind+arr[ind]<len(arr) and ind+arr[ind] not in visited:
                visited.add(ind+arr[ind])
                queue.append(ind+arr[ind])
        return False