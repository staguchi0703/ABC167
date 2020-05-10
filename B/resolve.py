def resolve():
    '''
    code here
    '''
    A, B, C, K = [int(item) for item in input().split()]

    A_max = min(A, K)
    B_max = min(B, K - A_max)
    C_max = K - A_max - B_max

    print(A_max - C_max)

if __name__ == "__main__":
    resolve()
