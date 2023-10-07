def sort_dictionary(myDict):

    if len(myDict) == 0:
        return
    else:
        reverseSorted = dict(sorted(myDict.items(), reverse=True))
        list = []
        for key, value in reverseSorted.items():
            list.append((key, value[0]))
        return list
 
    
    
myDict = {}

print(sort_dictionary(myDict))