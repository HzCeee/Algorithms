# Binary Search

```python
def binarySearch(nums, target):
	low, high = 0, len(nums) - 1
    while low <= high:
    	mid = (low + high) // 2
        if nums[mid] == target:
        	return mid
        elif nums[mid] < target: # condition 1
        	low = mid + 1
        else: # nums[mid] > target # condition 2
          	high = mid - 1
	return low
```

When while loop terminates, $low = high + 1$ and for all $i \leq low-1$, $nums[i] < target$ (condition 1), for all $j \geq high + 1$, $nums[j] > target$ (condition 2).

```python
def binarySearch(nums, target):
	low, high = 0, len(nums) - 1
    while low <= high:
    	mid = (low + high) // 2
        if nums[mid] <= target: # condition 1
        	low = mid + 1
        else: # nums[mid] > target # condition 2
          	high = mid - 1
	return low
```

Similarly, when while loop terminates, $low = high + 1$ and for all $i \leq low-1$, $nums[i] \leq target$ (condition 1), for all $j \geq high + 1$, $nums[j] > target$ (condition 2).

# Divide and Conquer

__Maximum Subarray__

```python
def devideAndConquer(nums):
  	if len(nums) == 1: # base case
      	return nums[0]
	left, right = 0, len(nums) - 1
    mid = (left + right) // 2
    leftMaxSum = devideAndConquer(nums[: mid+1]) # max sum in left subarray
    rightMaxSum = devideAndConquer(nums[mid+1:]) # max sum in right subarray
    
    leftInterSum, rightInterSum, leftMaxInterSum, rightMaxInterSum = \\
    0, 0, -float('inf'), -float('inf')
    for num in nums[: mid+1][::-1]:
      	leftInterSum += num
        leftMaxInterSum = max(leftMaxInterSum, leftInterSum)
    for num in nums[mid+1:]:
      	rightInterSum += num
        rightMaxInterSum = max(rightMaxInterSum, rightInterSum)
    midMaxSum = leftMaxInterSum + rightMaxInterSum # max sum in middle subarray
    return max(leftMaxSum, rightMaxSum, midMaxSum)
```

Note: `mid + 1`

# Dynammic Programming

1. Normal DP

__Maximum Subarray__

```python
def maxSubArray(nums):
  	# dp[index] denotes the maximum sum consisting of nums[index] in subarray nums[:index+1]
    # dp[index] = max(dp[index - 1] + nums[index], nums[index])
    minValue = -float('inf')
    dp = [minValue for i in range(len(nums))]
    dp[0] = nums[0]
    for index in range(1, len(nums)):
      	dp[index] = max(dp[index - 1], nums[index])
        
	return max(dp)
```

- First decide what dp[index] means.
- Then derive the relationship between dp[index] and all the other element in dp list.
- Finally compute each element in dp from start to end.

2. State Machine

__Best Time To Buy And Sell Stock With Cooldown__

```python
def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """

    # free[i] denotes the max profit on day[i] with no stock in hand
    # hold[i] denotes the max profit on day[i] with stock in hand
    # coolDown[i] denotes the max profit on day[i] in coolDown state
    #
    # free[i] = max(free[i - 1], coolDown[i - 1])
    # hold[i] = max(hold[i - 1], free[i - 1] - prices[i])
    # coolDown[i] = hold[i - 1] + prices[i]

    if not prices:
        return 0

    free, hold, coolDown = [0 for i in range(len(prices))], [0 for i in range(len(prices))], [0 for i in range(len(prices))]
    free[0], hold[0], coolDown[0] = 0, -prices[0], 0

    for i in range(1, len(prices)):
        free[i] = max(free[i - 1], coolDown[i - 1])
        hold[i] = max(hold[i - 1], free[i - 1] - prices[i])
        coolDown[i] = hold[i - 1] + prices[i]

    return max(free[-1], coolDown[-1])
```

# DFS

__Level Order Traversal__

- Recursion

```python
def levelOrderDFS(root):
  	depth = 0
    levelOrderTraversal = []
    
    def levelOrderDFSHelper(node, depth):
      	if not node: # reach leaf
          	return
        # process at current node
        if depth == len(levelOrderTraversal):
          	levelOrderTraversal.append([])
        levelOrderTraversal[depth].append(node.val)
        # search child node
        levelOrderDFSHelper(node.left, depth + 1)
        levelOrderDFSHelper(node.right, depth + 1)
        
    levelOrderDFSHelper(root, depth)
    return levelOrderTraversal
```

- Stack


```python
def levelOrderDFS(root):
  	depth = 0
    levelOrderTraversal = []
    
    nodeStack = [[root, depth]]
    
    while nodeStack:
      	# get current node
      	node, depth = nodeStack.pop()
        # process at current node
        if depth == len(levelOrderTraversal):
          	levelOrderTraversal.append([])
        levelOrderTraversal[depth].append(node.val)
        # search child node
        nodeStack.append([node.right, depth + 1])
        nodeStack.append([node.left, depth + 1])
        
  	return levelOrderTraversal
```

# BFS

__Check Symmetry__

```python
def isSymmetric(root):
  	nodeQueue = [root]
    while nodeQueue:
      	# process current layer
      	values = [node.val if node else None for node in nodeQueue]
        if values != values[::-1]:
          	return False
        # generate next layer node
        nodeQueue = [childNode for node in nodeQueue if node for childNode in [node.left, node.right]]
```

__Invert Binary Tree__

```python
def invertTree(self, root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
    if not root:
        return []

    nodeQueue = [root]
    while nodeQueue:
        node = nodeQueue.pop(0)
        if node:
            node.left, node.right = node.right, node.left
            nodeQueue.append(node.left)
            nodeQueue.append(node.right)
    return root
```

Note:

- Implement BFS by generating nodes in next layer
- Implement BFS by deque

# Two Pointer

1. Normal Two Pointer

__Merge Sorted Array__

```python
def merge(self, nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: void Do not return anything, modify nums1 in-place instead.
    """

    # index1 denotes the index of current compared numbers in nums1
    # index2 denotes the index of current compared numbers in nums2
    # curIndex denotes the index of current processed numbers in new nums1

    index1, index2, curIndex = m - 1, n - 1, m + n - 1

    while index1 >= 0 and index2 >= 0:
        if nums1[index1] > nums2[index2]:
            nums1[curIndex] = nums1[index1]
            index1 -= 1
            curIndex -= 1
        else:
            nums1[curIndex] = nums2[index2]
            index2 -= 1
            curIndex -= 1
    if index2 >= 0:
        nums1[:index2 + 1] = nums2[:index2 + 1]
```

2. Fast and Slow Pointer

__Linked List Cycle__

```python
def hasCycle(self, head):
    """
    :type head: ListNode
    :rtype: bool
    """

    lowPtr = fastPtr = head

    while fastPtr and fastPtr.next:
        fastPtr = fastPtr.next.next
        lowPtr = lowPtr.next
        if lowPtr == fastPtr:
            return True

    return False
```

__Linked List Cycle II__

```python
def detectCycle(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """

    '''
    Step 1: Determine whether there is a cycle
    1.1) Using a slow pointer that move forward 1 step each time
    1.2) Using a fast pointer that move forward 2 steps each time
    1.3) If the slow pointer and fast pointer both point to the same location after several moving steps, there is a cycle;
    1.4) Otherwise, if (fast->next == NULL || fast->next->next == NULL), there has no cycle.

    Step 2: If there is a cycle, return the entry location of the cycle
    2.1) L1 is defined as the distance between the head point and entry point
    2.2) L2 is defined as the distance between the entry point and the meeting point
    2.3) C is defined as the length of the cycle
    2.4) n is defined as the travel times of the fast pointer around the cycle When the first encounter of the slow pointer and the fast pointer
    According to the definition of L1, L2 and C, we can obtain:
    the total distance of the slow pointer traveled when encounter is L1 + L2
    the total distance of the fast pointer traveled when encounter is L1 + L2 + n * C
    Because the total distance the fast pointer traveled is twice as the slow pointer, Thus:
    2 * (L1+L2) = L1 + L2 + n * C => L1 + L2 = n * C => L1 = (n - 1) C + (C - L2)

    So, when the slow pointer and the fast pointer encounter in the cycle, we can define a pointer "entry" that point to the head, this "entry" pointer moves one step each time so as the slow pointer. When this "entry" pointer and the slow pointer both point to the same location, this location is the node where the cycle begins.
    '''

    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            entry = head
            while slow != entry:
                slow = slow.next
                entry = entry.next
            return entry
```

__FInd the Duplicate Number__

```python
def findDuplicate(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    '''
    "array nums containing n + 1 integers where each integer is between 1 and n (inclusive)" 
    makes the array an abstracted linked list: nums[num] -> newNum. 
    Now since integer cannot be 0, item 0 is guarenteed to be a "node" outside any cycle because nums[num] must be larger than 0. 
    Then the 1st fast-slow traverse is guranteed to have the meet point at equally distance from the common starting point (0) to the cycle entry point
    '''
    fastPtr = 0
    slowPtr = 0

    while (fastPtr == 0 and slowPtr == 0) or fastPtr != slowPtr:
        fastPtr, slowPtr = nums[nums[fastPtr]], nums[slowPtr]

    circleEntryPtr = 0 # the circle entry is a position of the duplicated numbers

    while circleEntryPtr != slowPtr:
        circleEntryPtr, slowPtr = nums[circleEntryPtr], nums[slowPtr]

    return circleEntryPtr
```

__Palidrome Linked List__

```python
def isPalindrome(self, head):
    """
    :type head: ListNode
    :rtype: bool
    """
    # fast is 2-pace pointer
    # slow is 1-pace pointer
    # reverse is the previous node before slow

    slow = fast = head
    reverse = None

    while fast and fast.next:
        fast = fast.next.next
        tmp = reverse
        reverse = slow
        slow = slow.next
        reverse.next = tmp

    if fast: # if odd number in list, slow is now the center number index
        slow = slow.next

    while reverse and slow:
        if reverse.val == slow.val:
            reverse = reverse.next
            slow = slow.next
        else:
            return False

    return True
```

Note:

- Fast and Slow Pointers can be used to detect cycle and find the middle point of a (linked) list.

----

1. Permutation of string can be stored in a dict() or a list

````python
def checkInclusion(self, s1, s2):
    """
    :type s1: str
    :type s2: str
    :rtype: bool
    """
    # leftPtr denotes the left index of the checked string
    # rightPtr denotes the index after the rightmost element of the checked string

    target = dict()
    for char in s1:
        target[char] = 1 if char not in target else target[char] + 1

    check = dict()
    for char in s2[: len(s1) - 1]:
        check[char] = 1 if char not in check else check[char] + 1

    leftPtr = 0

    for rightPtr in range(len(s1), len(s2) + 1):
        check[s2[rightPtr - 1]] = 1 if s2[rightPtr - 1] not in check else check[s2[rightPtr - 1]] + 1

        if check == target: return True

        check[s2[leftPtr]] -= 1
        if check[s2[leftPtr]] == 0: check.pop(s2[leftPtr])

        leftPtr += 1

    return False
````

