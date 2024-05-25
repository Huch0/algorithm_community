def solution(s):
    nums = list(map(int, s.split()))
    return '%d %d' % (min(nums), max(nums))
