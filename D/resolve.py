def resolve():
    '''
    code here
    '''
    import collections
    N, K = [int(item) for item in input().split()]
    A_list = [int(item) for item in input().split()]
    order_dict = dict(zip(range(1,N+1),A_list))

    foot_print = [-1 for _ in range(N+1)]
    loop_que = collections.deque([1])

    goto = 1

    while foot_print[goto] == -1:
        foot_print[goto] = 1
        goto = order_dict[goto]
        loop_que.append(goto) 

    loop_start = loop_que.index(goto) + 1
    loop_len = len(loop_que) - loop_start

    # print(loop_que)
    # print(loop_start, loop_len)


    data_list = list(loop_que)
    if K >= len(loop_que):
        temp_K = K - loop_start + 1
        temp_K %= loop_len
        temp_loop = data_list[loop_start-1:-1]
        print(temp_loop[temp_K])
    else:

        print(data_list[K])

if __name__ == "__main__":
    resolve()
