def merge_list(list1, list2):

    if not isinstance(list1, int) or isinstance(list2, int):
        return "Not a list of integet numbers"

    list3 = list1 + list2

    def sortList (list, left, right):
        if left < right:
            partition_pos = partition(list ,left, right)
            sortList(list, left, partition_pos - 1)
            sortList(list, partition_pos + 1, right)

    def partition(list, left, right):
        pivot = list[left]
        i = left
        j = right

        while i < j:
            while list[i] <= pivot:
                i+=1
            while list[j] > pivot:
                j-=1
            if i < j:
                temp = list[i]
                list[i] = list[j]
                list[j] = temp

        temp = list[left]
        list[left] = list[j]
        list[j] = temp
        return j

    sortList(list3, 0, len(list3) - 1)
    return list3

list1 = [1,5,3,7]
list2 = []


list4 = ['mars', 'lego']

print(merge_list(list1, list4))
