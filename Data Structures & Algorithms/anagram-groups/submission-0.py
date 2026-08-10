class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l = []
        for w1 in strs:
            w = []
            for w2 in strs:
                if sorted(list(w1)) == sorted(list(w2)):
                    w.append(w2)
            if w not in l:
                l.append(w)
        return l