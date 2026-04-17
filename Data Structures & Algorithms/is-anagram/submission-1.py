class Solution:
    def isAnagram(self, source: str, target: str) -> bool:
        if len(source) != len(target):
            return False

        char_count = {}
        for char in source:
            char_count[char] = char_count.get(char, 0) + 1

        for char in target:
            if char not in char_count:
                return False
            char_count[char] -= 1
            if char_count[char] < 0:
                return False
        return True
