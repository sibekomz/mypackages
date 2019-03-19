def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1,0,-1):
        for j in range(i):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
    '''Return array of items, sorted in ascending order'''

def merge_sort(items):
    if len(items) < 2:return items

    result,mid = [],int(len(items)/2)

    y = merge_sort(items[:mid])
    z = merge_sort(items[mid:])

    while (len(y) > 0) and (len(z) > 0):
            if y[0] > z[0]:result.append(z.pop(0))
            else:result.append(y.pop(0))
    result.extend(y+z)
    '''Return array of items, sorted in ascending order'''
    return result

def quick_sort(items):
    def quick_sort(l):
    if len(l) == 0:
        return l
    start = l[0]
    first = [x for x in l if x == start]
    smaller = quick_sort([x for x in l if x < start])
    larger = quick_sort([x for x in l if x > start])

    '''Return array o
    gnbfv dcswf items, sorted in ascending order'''
    return smaller + first + larger
