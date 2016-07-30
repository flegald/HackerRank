def save_the_prisoner(T):
    for i in range(T):
        N = input()
        M = input()
        S = input()
        def poison_sweets(N, M, S):
            prisoners = []
            for i in range(N):
                prisoners.append(i + 1)
            idx = S - 1
            check = True
            for i in range(M):
                if i == M - 1:
                    if check:
                        print(prisoners[idx - 1])
                        return prisoners[idx - 1]
                    else:
                        print(prisoners[idx])
                        return prisoners[idx]
                if prisoners[idx] == prisoners[-1]:
                    idx = 0
                    check = False
                else:
                    idx += 1
        poison_sweets(N,M,S)
