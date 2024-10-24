#Author: Tianyi Xu
#Homework problems for third week of leetcode bootcamp

class Solution:
    #234. Palindrome Linked List
    def isPalindrome(self, head) -> bool:
        myLst = []
        while (head is not None):
            myLst.append(head.val)
            head = head.next
        for i in range(len(myLst)//2 + 1):
            if myLst[i] != myLst[len(myLst)-1-i]:
                return False
        return True
    
    #19. Remove Nth Node From End of List
    def removeNthFromEnd(self, head, n: int):
        cursor = head
        length = 0
        while cursor is not None:
            cursor = cursor.next
            length += 1
        if length == n:
            head = head.next
        else:
            prev = head
            for i in range(length - n - 1):
                prev = prev.next
            prev.next = prev.next.next
        return head

    # 73. Set Matrix Zeroes
    # O(1) space?
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        column1 = 1
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    if j == 0:
                        column1 = 0
                    else:
                        matrix[0][j] = 0
        for i in range(1, len(matrix)):
            if (matrix[i][0] == 0):
                for j in range(len(matrix[i])):
                    matrix[i][j] = 0
        for j in range(1, len(matrix[0])):
            if (matrix[0][j] == 0):
                for i in range(len(matrix)):
                    matrix[i][j] = 0
        if matrix[0][0] == 0:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0       
        if (column1 == 0):
            for i in range(len(matrix)):
                matrix[i][0] = 0

    # O(m+n) space
        """
    def setZeroes(self, matrix) -> None:
        iSet = set()
        jSet = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    iSet.add(i)
                    jSet.add(j)
        for i in iSet:
            for iSub in range(len(matrix[i])):
                matrix[i][iSub] = 0
        for j in jSet:
            for jSuper in range(len(matrix)):
                matrix[jSuper][j] = 0
        """
    
    
    # O(mn) space
    '''
    def setZeroes(self, matrix) -> None:
        ind = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    ind.append((i,j))
        for i, j in ind:
            for iSub in range(len(matrix[i])):
                matrix[i][iSub] = 0
            for jSuper in range(len(matrix)):
                matrix[jSuper][j] = 0
    '''
