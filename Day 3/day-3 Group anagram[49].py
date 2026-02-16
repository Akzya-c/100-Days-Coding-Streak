class Solution(object):
    def groupAnagrams(self, strs):
        group={}
        for word in strs:
            key=''.join(sorted(word))
            if key not in group:
                group[key]=[]
            group[key].append(word)
        return group.values()
