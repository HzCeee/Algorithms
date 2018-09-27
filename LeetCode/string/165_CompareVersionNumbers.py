class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        subVersion1 = version1.split(".")
        subVersion2 = version2.split(".")
        for i in range(min(len(subVersion1), len(subVersion2))):
            if int(subVersion1[i]) == int(subVersion2[i]):
                continue
            return 1 if int(subVersion1[i]) > int(subVersion2[i]) else -1
        if len(subVersion1) == len(subVersion2):
            return 0
        elif len(subVersion1) > len(subVersion2):
            return 0 if all(map(lambda x: int(x) == 0, subVersion1[i+1:])) else 1
        else:
            return 0 if all(map(lambda x: int(x) == 0, subVersion2[i+1:])) else -1