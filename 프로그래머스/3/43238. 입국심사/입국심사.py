def solution(n, times):
    left, right = 1, max(times) * n
    while left < right:
        mid = (left+right) // 2
        done = 0
        for t in times:
            done += mid // t
            if done >= n:
                break
        if done >= n:
            right = mid
        else:
            left = mid + 1
    return left