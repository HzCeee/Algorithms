class Solution:
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        nameAccountInfo = {}
        for accountInfo in accounts:
            name, account = accountInfo[0], set(accountInfo[1:])
            if name not in nameAccountInfo:
                nameAccountInfo[name] = [account]
            else:
                distinctSetIndex, overlappedSetIndex = [], []
                for index, recoredAccount in enumerate(nameAccountInfo[name]):
                    if len(recoredAccount.intersection(account)) == 0:
                        distinctSetIndex.append(index)
                    else:
                        overlappedSetIndex.append(index)
                newAccountRecordOverlapped = account
                for index in overlappedSetIndex:
                    newAccountRecordOverlapped = newAccountRecordOverlapped.union(nameAccountInfo[name][index])
                newAccountRecordDistinct = [nameAccountInfo[name][index] for index in distinctSetIndex]
                nameAccountInfo[name] = [*newAccountRecordDistinct, newAccountRecordOverlapped]
        
        ans = []
        for name, accounts in nameAccountInfo.items():
            for account in accounts:
                ans.append([name, *sorted(list(account))])
        
        return ans