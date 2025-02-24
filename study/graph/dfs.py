import sys
input = sys.stdin.readline


# 그래프 array, 시작 위치, 방문 정보가 들어있는 리스트
def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=" ")
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:  # graph[i]에 있는 원소가 방문되어 있지 않다면 재귀함수 호출
            dfs(graph, i, visited)


if __name__ == '__main__':
    n, m, s = map(int, input().split())
    graph = [[] for _ in range(n+1)]

    for _ in range(m):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)    # 비방향

    visited = [False] * (n+1)

    dfs(graph, s, visited)