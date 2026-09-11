class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        first = strs[0]
        prefix = ""

        for i in range(len(first)):
            for word in strs[1:]:

                if i == len(word) or word[i] != first[i]:
                    return prefix

            prefix += first[i]
        return prefix