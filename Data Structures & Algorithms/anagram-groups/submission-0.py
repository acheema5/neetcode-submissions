class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = {}

        for word in strs:
            key = [0] * 26
            for c in word:
                key[ord(c) - ord('a')] += 1
            
            if tuple(key) not in m:
                m[tuple(key)] = []
            m[tuple(key)].append(word)
        
        return list(m.values())