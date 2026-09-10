class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap={}
        for i in range(len(strs)):
            word=strs[i]
            key="".join(sorted(word))
            if key not in  hashmap:
                hashmap[key]=[]
            hashmap[key].append(word)
        return list(hashmap.values())
        