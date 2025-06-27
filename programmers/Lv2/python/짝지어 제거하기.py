def solution(s):
    answer = []

    for c in s:
        if (not answer) or (answer[-1] != c):
            answer.append(c)
        else:
            answer.pop()

    return 0 if answer else 1
