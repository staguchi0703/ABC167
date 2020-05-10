def resolve():
    '''
    code here
    '''
    S = input()
    T = input()

    if len(T) == len(S) + 1 and S == T[:-1]:
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    resolve()
