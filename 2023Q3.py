from copy import deepcopy
from collections import deque
def BFS():
    start = list(map(lambda x:list(map(int, list(x))), input().split()))
    end = list(map(lambda x:list(map(int, list(x))), input().split()))

    q = deque()
    visited = set()
    for i in range(0, len(start)):
        start[i] = tuple(start[i])
    for i in range(0, len(end)):
        end[i] = tuple(end[i])
    end = tuple(end)

    q.append((tuple(start), 0))
    while q:
        state, moves = q.popleft()
        if state == end:
            return moves
        if state in visited:
            continue
        visited.add(state)
        state = list(state)
        for i in range(0, len(state)):
            state[i] = list(state[i])
        for x in range(0, len(state)):
            for y in range(0, len(state)):
                if x == y:
                    continue
                if state[x] == [0]:
                    continue
                temp = deepcopy(state)
                move = temp[x].pop()
                if temp[y] == [0]:
                    temp[y] = [move]
                else:
                    temp[y].append(move)
                if len(temp[x]) == 0:
                    temp[x] = [0]
                for i in range(0, len(temp)):
                    temp[i] = tuple(temp[i])
                if tuple(temp) == end:
                    return moves + 1
                q.append((tuple(temp), moves+1))

print(BFS())