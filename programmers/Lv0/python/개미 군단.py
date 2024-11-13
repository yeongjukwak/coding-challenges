def solution(hp):
    return (hp // 5) + sum(divmod(int(hp % 5), 3))
