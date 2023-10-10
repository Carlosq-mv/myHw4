def cacti_number(func):
    def wrapper(array):
        if len(array) == 0 or len(array[0]) == 0:
            return 0 
        
        
        
        
        
        return wrapper
            

def main():
    plot = [[1, 0, 1, 0, 1],
            [0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0]]
    
    plot2 = [[0, 1, 0, 0, 0, 0],
             [0, 0, 0, 1, 0, 0],
             [1, 0, 1, 0, 0, 1]]
    
    print(cacti_number(plot))


main()
















