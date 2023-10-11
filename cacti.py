def cacti_number(func):
    def wrapper(array):
        if len(array) == 0 or len(array[0]) == 0:
            return 0

        rows, cols = len(array), len(array[0])
        num_cacti_planted = 0

        for row in range(rows):
            for col in range(cols):
                if array[row][col] == 0:
                    is_valid = True
                    for dx in [-1, 0, 1]:
                        for dy in [-1, 0, 1]:
                            if dx != 0 or dy != 0:
                                x, y = row + dx, col + dy
                                if 0 <= x < rows and 0 <= y < cols and array[x][y] == 1:
                                    is_valid = False
                                    break
                    if is_valid:
                        num_cacti_planted += 1
        return num_cacti_planted

    return wrapper


