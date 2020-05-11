def resolve():
    '''
    code here
    '''
    N, K = [int(item) for item in input().split()]
    A_list = [int(item) for item in input().split()]

    bit_k = bin(K)[2:]

    telepo_list = [A_list]

    for _ in range(len(bit_k)-1):
        temp_list = telepo_list[-1]
        new_telep = [temp_list[i-1] for i in temp_list]
        telepo_list.append(new_telep)

    # print(telepo_list)

    goto = 1
    for i in range(len(bit_k)):
        temp_list = telepo_list[i]
        if ((K >> i) & 1):
            goto = temp_list[goto - 1]
            # print(i, goto)

    print(goto)


if __name__ == "__main__":
    resolve()
