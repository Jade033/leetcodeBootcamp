def twoSum(numbers, target):
    start = 0
    end = len(numbers) - 1
    while start < end:
        if (numbers[start] + numbers[end] == target):
            return [start + 1, end + 1]
        elif (numbers[start] + numbers[end] < target):
            start += 1
        else:
            end -= 1 

def productExceptSelf(nums):
    leftPro = 1
    rightPro = 1
    result = [1]*len(nums)
    leftInd = 1
    rightInd = len(result) - 2
    leftCursor = 0
    rightCursor = len(nums) - 1
    while leftInd < len(result):
        leftPro *= nums[leftCursor]
        rightPro *= nums[rightCursor]
        leftCursor += 1
        rightCursor -= 1
        result[leftInd] *= leftPro
        result[rightInd] *= rightPro
        leftInd += 1
        rightInd -= 1
    return result

def sortColors(nums):
    cursor = 1
    while cursor < len(nums):
        i = cursor
        while (i > 0) and (nums[i] < nums[i-1]):
            nums[i], nums[i-1] = nums[i-1], nums[i]
            i -= 1
        cursor += 1





