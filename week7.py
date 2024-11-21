# Author: Tianyi Xu
# Homework solutions for seventh week


from collections import deque
class Solution:
    # 199. Binary Tree Right Side View
    # Return what you would see if you look from the right side of the tree
    # Not very hard. Stardard level-order traversal
    def rightSideView(self, root):
        level = 0
        currVal = -101
        queue = deque()
        if root is None:
            return []
        queue.append((root, level))
        result = []
        while queue:
            tempNode, tempLv = queue.popleft()
            if (tempLv == level):
                currVal = tempNode.val
            else:
                result.append(currVal)
                currVal = tempNode.val
                level += 1
            if (tempNode.left):
                queue.append((tempNode.left, tempLv + 1))
            if (tempNode.right):
                queue.append((tempNode.right, tempLv + 1))
        result.append(currVal)
        return result

    # 994. Rotting Oranges
    # Rotten Orange would infect surrounding 4-directionally adjacent oranges
    # 2D matrix with 0 representing an empty cell, 1 representing a fresh orange,
    # and 2 representing a rotten orange
    # Pretty interesting. Solved using bfs algorithm
    def orangesRotting(self, grid) -> int:
        time = -1
        queue = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i,j))
        # This part is done to correctly return 0 for a matrix of only zeros
        if (not queue):
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 1:
                        return -1
            return 0
            
        while (queue):
            tempQ = deque()
            for location in queue:
                tempQ.append(location)
            while tempQ:
                i, j = tempQ.popleft()
                queue.popleft()
                if (i - 1 >= 0):
                    if (grid[i-1][j] == 1):
                        queue.append((i-1,j))
                        grid[i-1][j] = 2
                if (i + 1 < len(grid)):
                    if (grid[i+1][j] == 1):
                        queue.append((i+1,j))
                        grid[i+1][j] = 2
                if (j - 1 >= 0):
                    if (grid[i][j-1] == 1):
                        queue.append((i,j-1))
                        grid[i][j-1] = 2
                if (j + 1 < len(grid[0])):
                    if (grid[i][j+1] == 1):
                        queue.append((i,j+1))
                        grid[i][j+1] = 2
            time += 1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        return time

    # 210. Course Schedule II
    # Pretty interesting, though not very hard to come up with the iddea         
    def findOrder(self, numCourses: int, prerequisites):
        baseS = set()
        sus = set() # used to deal with one course having multiple prerequisites
        myLst = [0]*numCourses
        for target, prereq in prerequisites:
            myLst[target] = 1
        for i in range(len(myLst)):
            if myLst[i]  == 0:
                baseS.add(i)
        tempS = baseS.copy() # used to store a temporary level of data
        result = []
        if not baseS:
            return result
        while baseS:
            for i in range(len(prerequisites)):
                if prerequisites[i][1] in tempS:
                    sus.add(prerequisites[i][0])
                    prerequisites[i] = [-1, -1]
            for target, prereq in prerequisites:
                sus.discard(target)
            baseS.update(sus)
            sus.clear()
            result.extend(tempS)
            baseS -= tempS
            tempS = baseS.copy()
        for target, prereq in prerequisites:
            if target >= 0:
                return []
        return result
            
            
        