class Solution:
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        groups = dict()
        for string in strings:
            pattern = tuple([0] + [(ord(string[i]) - ord(string[i-1])) % (ord("z")-ord("a")+1) for i in range(1, len(string))])
            if pattern not in groups:
                groups[pattern] = []
            groups[pattern].append(string)
        return list(groups.values())
        