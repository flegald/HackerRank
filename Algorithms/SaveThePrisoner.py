def poison_sweets(N, M, S):
     prisoners = []
     for i in range(N):
         prisoners.append(i + 1)
         
     idx = S - 1
     for i in range(M):
         if i == M - 1:
             print(prisoners[idx])
         if prisoners[idx] == prisoners[-1]:
             idx = 0
         else:
             idx += 1
