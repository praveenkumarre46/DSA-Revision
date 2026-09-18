class Solution:

  def maxNumOfSubstrings(self, s: str) -> list[str]:
    first = {}
    last = {}
    for i, c in enumerate(s):
      if c not in first:
        first[c] = i
      last[c] = i

    intervals = []
    for c in first:
      start = first[c]
      right = last[c]
      valid = True

      k = start
      while k <= right:
        char = s[k]
        if first[char] < start:
          valid = False
          break
        right = max(right, last[char])
        k += 1

      if valid:
        intervals.append((start, right))

    intervals.sort(key=lambda x: x[1])

    ans = []
    prev_end = -1
    for start, end in intervals:
      if start > prev_end:
        ans.append(s[start : end + 1])
        prev_end = end

    return ans