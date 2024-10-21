def solution(s):
    numbers = [int(number) for number in s.split(' ')]
    return '{0} {1}'.format(min(numbers), max(numbers))
