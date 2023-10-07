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
    
list1 = [1,5,52,83]
list2 = [2,6,7,8]

list3 = [-8,1,2,70,71]
list4 = [-20,-19,68]

list5 = [2]
list6 = [1]

list7 = [random.randint(1, 1000) for _ in range(500)]
list8 = [random.randint(1, 1000) for _ in range(500)]

listA = ['mars', 'lego']
listB= ['sdf', 'sdf']

list9= []
result = merge_list(list7, list8)
print(result)
