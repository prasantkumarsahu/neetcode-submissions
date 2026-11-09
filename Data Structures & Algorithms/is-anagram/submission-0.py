class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        occorance = {}

        for ch in s:
            occorance[ch] = occorance.setdefault(ch, 0) + 1

        for ch in t:
            occorance[ch] = occorance.get(ch, 0) - 1
        
        for oc in occorance:
            if occorance[oc] != 0:
                return False

        return True