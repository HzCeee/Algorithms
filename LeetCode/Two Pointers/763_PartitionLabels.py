def partitionLabels(self, S):
    """
    :type S: str
    :rtype: List[int]
    """
    
    # leftPtr and righrPtr denotes the start and end of the current partition
    # curPtr denotes the current checked index
    
    lastOccurence = {char: curPtr for curPtr, char in enumerate(S)}
    
    rightPtr = leftPtr = 0
    ans = []
    for curPtr, char in enumerate(S):
        rightPtr = max(rightPtr, lastOccurence[char])
        if curPtr == rightPtr:
            ans.append(curPtr - leftPtr + 1)
            leftPtr = curPtr + 1
        
    return ans