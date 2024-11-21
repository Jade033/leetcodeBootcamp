# Author: Tianyi Xu
# Homework problems for sixth week of leetcode bootcamp

import heapq
class Solution:
    # 236. Lowest Common Ancestor of a Binary Tree
    def lowestCommonAncestor(self, root, p, q):
        if (root is None) or (root == p) or (root == q) :
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        return root if (left and right) else (left or right)
    
    # 347. Top K Frequent Elements
    def topKFrequent(self, nums, k):
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        myHeap = []
        for num, freq in freq.items():
            heapq.heappush(myHeap, (freq, num))
        most_freq = heapq.nlargest(k, myHeap)
        result = [num for freq, num in most_freq]
        return result
    
    