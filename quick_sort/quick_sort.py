'''
quick sort
'''

def quick_sort(sort_list, left, right):
    ''' main function '''
    if left > right:
        return None
    temp = sort_list[left]
    l_f = left
    r_t = right
    while l_f != r_t:
        while(sort_list[r_t] >= temp and l_f < r_t):
            r_t -= 1
        while(sort_list[l_f] <= temp and l_f < r_t):
            l_f += 1
        print("{},left is {},right is {}".format(sort_list, sort_list[l_f], sort_list[r_t]))

        if l_f < r_t:
            sort_list[l_f], sort_list[r_t] = sort_list[r_t], sort_list[l_f]

    sort_list[left], sort_list[l_f] = sort_list[l_f], sort_list[left]
    quick_sort(sort_list, left, l_f-1)
    quick_sort(sort_list, r_t+1, right)
    return sort_list
