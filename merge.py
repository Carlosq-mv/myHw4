import random
def merge_list(list1, list2):

    try:
        for i, j in zip(list1, list2):
            if not isinstance(i, int) or not isinstance(j, int):
                raise TypeError("TypeError")
    except TypeError as error:
        return error

    def sortList(list):
        if len(list) > 1:
            left = list[:len(list)//2]
            right = list[len(list)//2:]
            
            sortList(left)
            sortList(right)
            
            i,j, k = 0, 0, 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    list[k] = left[i]
                    i += 1
                else:
                    list[k] = right[j]     
                    j += 1      
                k += 1
            while i < len(left):
                list[k] = left[i]
                i += 1
                k += 1
                
            while j < len(right):
                list[k] = right[j]
                j += 1
                k += 1
                
    list3 = list1 + list2
    sortList(list3)
    return list3
    