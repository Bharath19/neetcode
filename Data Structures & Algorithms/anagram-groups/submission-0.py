class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def is_anagram(s1: str, s2: str) -> bool:
            if len(s1) != len(s2):
                return False

            count = [0] * 26

            for ch in s1:
                count[ord(ch) - ord('a')] += 1

            for ch in s2:
                count[ord(ch) - ord('a')] -= 1

            for num in count:
                if num != 0:
                    return False

            return True

        visited = [False] * len(strs)
        result = []

        for i in range(len(strs)):
            if visited[i]:
                continue

            group = [strs[i]]
            visited[i] = True

            for j in range(i + 1, len(strs)):
                if not visited[j] and is_anagram(strs[i], strs[j]):
                    group.append(strs[j])
                    visited[j] = True

            result.append(group)

        return result