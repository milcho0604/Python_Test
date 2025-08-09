import sys

def compute_ranks(people):
    """
    people: [(w, h), (w, h), ...]
    return: 각 사람의 등수 리스트
    """
    n = len(people)
    ranks = [0] * n

    for i in range(n):
        w_i, h_i = people[i]
        rank = 1  # 기본 1등에서 시작
        for j in range(n):
            if i == j:
                continue  # 자기 자신은 비교 제외
            w_j, h_j = people[j]
            if w_j > w_i and h_j > h_i:  # 둘 다 더 크면 i의 등수 하나 내려감
                rank += 1
        ranks[i] = rank
    return ranks


# ---- 입력/출력부 (백준 스타일) ----
input = sys.stdin.readline

n = int(input().strip())
people = [tuple(map(int, input().split())) for _ in range(n)]

ranks = compute_ranks(people)
print(*ranks)  # 공백 구분으로 한 줄 출력
