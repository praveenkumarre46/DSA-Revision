from collections import defaultdict, deque
from typing import List

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        words = set(wordList)
        if endWord not in words:
            return []
        
        words.discard(beginWord)
        

        parents = defaultdict(list)
        layer = {beginWord}
        found = False
        
        while layer and not found:
            words -= layer
            next_layer = set()
            
            for word in layer:
                if word == endWord:
                    found = True
                    break
                
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        if c == word[i]:
                            continue
                        next_word = word[:i] + c + word[i+1:]
                        if next_word in words:
                            next_layer.add(next_word)
                            parents[next_word].append(word)
                            
            layer = next_layer
            
        if not found:
            return []
            

        res = []
        
        def backtrack(curr_word, path):
            if curr_word == beginWord:
                res.append(path[::-1])
                return
            
            for p in parents[curr_word]:
                path.append(p)
                backtrack(p, path)
                path.pop()
                
        backtrack(endWord, [endWord])
        return res