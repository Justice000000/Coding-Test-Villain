# https://school.programmers.co.kr/learn/courses/30/lessons/181918

def solution(arr):

    stk = []
    i = 0

    while True:
        if i >= len(arr):
            break
        if not stk:
            stk.append(arr[i])
            i += 1
        if stk:
            if stk[-1] < arr[i]:
                stk.append(arr[i])
                i += 1
            else:
                stk.pop()

    return stk
