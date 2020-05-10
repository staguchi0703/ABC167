def resolve():
    '''
    code here
    '''
    import math
    N, M, K = [int(item) for item in input().split()]
    num_list = range(1, N+1)
    temp_fact = math.factorial(N)//math.factorial(N-M)

    res = 0
    for k in range(1,K+1):
        res += k*temp_fact
        res = res  % 998244353

    print(res)


if __name__ == "__main__":
    resolve()
