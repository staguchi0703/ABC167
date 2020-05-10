def resolve():
    '''
    code here
    '''

    N, M, X = [int(item) for item in input().split()]
    data = [[int(item) for item in input().split()] for _ in range(N)]

    cost = 10**9

    for i in range(2**N):
        temp_point = [0 for _ in range(M)]
        temp_cost = 0
        for j in range(N):
            if ((i >> j) & 1):
                for k, v in enumerate(data[j][1:]):
                    temp_point[k] += v
                temp_cost += data[j][0]

        is_flag = True
        for temp_p in temp_point:
            if temp_p < X:
                is_flag = False
                break
        
        if is_flag:
            cost = min(cost, temp_cost)

    if cost == 10**9:
        print(-1)
    else:
        print(cost)

if __name__ == "__main__":
    resolve()
