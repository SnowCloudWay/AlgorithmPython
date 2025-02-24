import sys
from collections import deque
input = sys.stdin.readline


def bfs(graph, start, visited):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    que = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while que:
        # 큐에서 하나의 원소를 뽑아 출력하기
        v = que.popleft()
        print(v, end=" ")
        # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                que.append(i)
                visited[i] = True


if __name__ == '__main__':
    n, m, s = map(int, input().split())
    graph = [[] for _ in range(n+1)]

    for _ in range(m):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)    # 비방향

    visited = [False] * (n+1)

    bfs(graph, s, visited)