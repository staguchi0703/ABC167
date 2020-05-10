def resolve():
    '''
    code here
    '''
    N, K = [int(item) for item in input().split()]
    A_list = [int(item) for item in input().split()]
    order_dict = dict(zip(range(1,N+1),A_list))

    foot_print = []

    goto = 1
    for i in range(N):
        if goto in foot_print:
            break
        else:
            foot_print.append(goto)
            goto = order_dict[goto]

    if K > len(foot_print):
        foot_print2 = []
        for i in range(N):
            if goto in foot_print2:
                break
            else:
                foot_print2.append(goto)
                goto = order_dict[goto]



        temp_num = K -len(foot_print)
        temp_num = temp_num % len(foot_print2)
        for i in range(temp_num):
            goto = order_dict[goto]

    print(goto)
if __name__ == "__main__":
    resolve()
