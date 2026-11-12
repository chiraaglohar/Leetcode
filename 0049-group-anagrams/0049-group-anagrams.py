class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 
                  31, 37, 41, 43, 47, 53, 59, 61, 67, 
                  71, 73, 79, 83, 89, 97, 101]        

        groups = {}
        for s in strs:
            m = 1
            for c in s:
                m *= primes[ord(c) - ord('a')]
            if m not in groups:
                groups[m] = []
            groups[m].append(s)

        return [v for v in groups.values()]
