class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}

        for str in strs:
            sorted_str = "".join(sorted(str))

            group.setdefault(sorted_str, []).append(str)

        return list(group.values())
