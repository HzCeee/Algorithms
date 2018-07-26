class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # return list of possible valid IP address combinations.
        def restoreIpAddressesHelper(secNo, IPAddress):
            if secNo == 4:
                if len(IPAddress) >= 4 or len(IPAddress) == 0:
                    return (False, [])
                elif len(IPAddress) == 1:
                    return (True, [IPAddress])
                elif len(IPAddress) == 2 or len(IPAddress) == 3:
                    return (True, [IPAddress]) if IPAddress[0] != "0" and int(IPAddress) <= 255 else (False, [])
                
            res = []
            for secLength in [1, 2, 3]:
                if not ((len(IPAddress[:secLength]) == 2 or len(IPAddress[:secLength]) == 3) \
                and (IPAddress[:secLength][0] == "0" or int(IPAddress[:secLength]) > 255)):
                    valid, combinations = restoreIpAddressesHelper(secNo+1, IPAddress[secLength:])
                    if valid:
                        for combination in combinations:
                            res.append(IPAddress[:secLength] + "." + combination)
                            
            return (True if res else False, res)
        
        return restoreIpAddressesHelper(1, s)[1]