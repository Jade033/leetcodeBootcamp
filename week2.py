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
