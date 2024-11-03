#Author: Tianyi Xu
#Homework problems for fourth week of leetcode bootcamp
from collections import *
class Solution:

    # 232. Implement Queue using (two) Stacks
    class MyQueue:

        def __init__(self):
            self.stack = []
            self.fakeQ = []
            

        def push(self, x: int) -> None:
            self.stack.append(x)
            

        def pop(self) -> int:
            if not self.fakeQ:
                while self.stack:
                    self.fakeQ.append(self.stack.pop())
            return self.fakeQ.pop()
            

        def peek(self) -> int:
            if not self.fakeQ:
                while self.stack:
                    self.fakeQ.append(self.stack.pop())
            return self.fakeQ[-1]
            

        def empty(self) -> bool:
            return (len(self.stack) + len(self.fakeQ)) == 0

    # 394. Decode String i.e. Input: s = "3[a]2[bc]"; Output: "aaabcbc"
    def decodeString(self, s: str) -> str:
        from collections import deque
        myStack = []
        for char in s:
            if char == ']':
                tempChar = myStack.pop()
                tempQueue = deque()
                while (myStack) and tempChar != '[':
                    tempQueue.appendleft(tempChar)
                    tempChar = myStack.pop()
                tempNum = []
                while (myStack) and (myStack[-1].isdigit()):
                    tempNum.append(myStack.pop())
                tempNum.reverse()
                multiple = int(''.join(tempNum))
                myStack.extend([char for _ in range(multiple) for char in tempQueue])
            else:
                myStack.append(char)
        return ''.join(myStack)
    
    #2327. Number of People Aware of a Secret
    #This is a math problem...
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        days = 1
        q, wait = defaultdict(int), defaultdict(list)
        total = 0
        wait[days + delay] = [days, 1]
        while (wait or q) and days <= n:
            if days in q:
                total -= q.pop(days)
            if days in wait:
                i, count = wait[days]
                q[i + forget] = count
                total += count
                wait.pop(days)
            if total:
                wait[days + delay] = [days, total]    
            days += 1
        cur = sum(q.values()) + sum([ count for _, count in  wait.values()])
        return cur % (10**9 + 7)