class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}

        for s in strs:
            count = [0] * 26

            for ch in s:
                count[ord(ch) - ord("a")] += 1

            group.setdefault(tuple(count), []).append(s)

        return list(group.values())
