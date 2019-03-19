def bubble_sort(items):

    '''Return array of items, sorted in ascending order'''
    exchanges = True
    i = len(items)-1
    while i > 0 and exchanges:
        exchanges = False
        for j in range(i):
            if items[j]>items[j+1]:
                exchanges = True
                items[j], items[j+1] = items[j+1], items[j]
                i -= 1
                print(items)

def merge_sort(items):

    '''Return array of items, sorted in ascending order'''

def quick_sort(items):

    '''Return array o
    gnbfv dcswf items, sorted in ascending order'''
