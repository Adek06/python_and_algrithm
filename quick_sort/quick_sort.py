'''
quick sort
'''
SORT_LIST = [1,5,2,7,0,8]

def quick_sort(left, right):
    ''' main function '''
    if left > right:
        return
    temp = SORT_LIST[left]
    l_f = left
    r_t = right
    while l_f != r_t:
        while(SORT_LIST[r_t] >= temp and l_f < r_t):
            r_t -= 1
        while(SORT_LIST[l_f] <= temp and l_f < r_t):
            l_f += 1
        if l_f < r_t:
            SORT_LIST[l_f] ,SORT_LIST[r_t] = SORT_LIST[r_t], SORT_LIST[l_f]
        print("{},left is {},right is {}".format(SORT_LIST,SORT_LIST[l_f],SORT_LIST[r_t]))

    SORT_LIST[left], SORT_LIST[l_f] = SORT_LIST[l_f], temp
    quick_sort(left, l_f-1)
    quick_sort(r_t+1, right)


if __name__ == "__main__":
    quick_sort(0,len(SORT_LIST)-1)
    print(SORT_LIST)