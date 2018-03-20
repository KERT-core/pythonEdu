def solution(num):
    if num < 0:
        num = int(str(num)[::-1][-1] + str(num)[::-1][:-1])
    else :
        num = int(str(num)[::-1])
    num = 0 if abs(num) > 0x7FFFFFFF else num
    return num
