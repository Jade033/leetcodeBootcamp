#Author: Tianyi Xu
#Homework problems for second week of leetcode bootcamp
#Leetcode 8 String to Integet (atoi)
def myAtoi(s):
    s = s.lstrip()
    ind = 0
    temp = 0
    if s and (s[0] == '+' or s[0] == '-'):
        ind = 1
        temp = 1
    while ind < len(s) and s[ind].isdigit():
        ind += 1
    if ind == temp or not s:
        return 0
    else:
        result = int(s[:ind])
        if result > 2**31 - 1:
            result = 2**31 - 1
        elif result < -2**31:
            result = -2**31
    return result

#Leetcode 438 Find all anagrams in a string
def findAnagrams(s, p):
    pDict = {}
    for char in p:
        if char in pDict:
            pDict[char] += 1
        else:
            pDict[char] = 1
    if len(s) < len(p):
        return []
    result = []
    sDict = {}
    for i in range(len(p) - 1):
        if s[i] in sDict:
            sDict[s[i]] += 1
        else:
            sDict[s[i]] = 1
    j = 0
    while s and p and (j < (len(s) - len(p) + 1)):
        if s[j + len(p) - 1] in sDict:
            sDict[s[j + len(p) - 1]] += 1
        else:
            sDict[s[j + len(p) - 1]] = 1
        if sDict == pDict:
            result.append(j)
        #print(sDict)
        sDict[s[j]] -= 1
        if sDict[s[j]] == 0:
            del sDict[s[j]]
        j += 1
    return result

#Leetcode 151 Reverse Words in a String
def reverseWords(s):
    s = s.strip()
    myLst = s.split()
    myLst.reverse()
    myStr = ' '.join(myLst)
    return myStr

#print(reverseWords("  hello world  "))

#print(findAnagrams('cbaebabacd', 'bac'))

'''
O(mn) time complexity. Exceeds time limit
def findAnagrams(s, p):
    def areAnagram(a, b):
        myDict = {}
        for char in a:
            if char in myDict:
                myDict[char] += 1
            else:
                myDict[char] = 1
        for char in b:
            if char not in myDict:
                return False
            else:
                myDict[char] -= 1
        for value in myDict.values():
            if value != 0:
                return False
        return True
    result = []
    i = 0
    while s and p and (i < (len(s) - len(p) + 1)):
        if areAnagram(s[i:i+len(p)], p):
            result.append(i)
        i += 1
    return result
'''

