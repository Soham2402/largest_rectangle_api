def calculate_max_rectangle(array):
     
    #used finding the biggest rectangle in a histogram's logic 
    stack = []
    max_area = 0
    for width, height in enumerate(array):
        start = width
        while stack and (stack[-1][1] > height):
            prev_start, prev_height = stack.pop()
            prev_width = width - prev_start
            if(prev_height == prev_width): # since the height and width cannot be equal
                prev_height -=1 # I eliminated an entire row to calculate the height 
            max_area = max(max_area, prev_height * prev_width)
            start = prev_start
        stack.append([start, height])
    # Check remaining rectangles in the stack
    for start, height in stack:
        width = len(array) - start
        if height == width:
            height -=1
        max_area = max(max_area, height * width)

    return max_area


def chose_hist(hist_array):  #this parses the hist_array i generated
    max_rect = [0,float('-inf')]
    histogram = []
    hash_array = list(hist_array)
    hash_array.append("x")
    for index in range(len(hash_array)-1):
        curr_val = hash_array[index][0]
        next_val = hash_array[index+1][0]
        if curr_val != next_val:
            histogram.append(hash_array[index][1])
            rectangle = calculate_max_rectangle(histogram)
            if rectangle > max_rect[1]:
                max_rect[1] = rectangle
                max_rect[0] = curr_val
            histogram = []
        elif len(histogram) == 0 or curr_val == next_val:
            histogram.append(hash_array[index][1])
    return max_rect


def calculate_histogram(matrix):
    hist_array = []
    max_rectangle = [0,0]
    for array in matrix:
        for index in range(len(array)):
            if len(hist_array) == index:
                hist_array.append([array[index],1])
            elif hist_array[index][0] ==  array[index]:
                hist_array[index][1] += 1
            elif hist_array[index][0] !=  array[index]:
                hist_array[index][0] = array[index]
                hist_array[index][1] = 1  
        curr_rectangle = chose_hist(hist_array)
        
        if curr_rectangle[1] > max_rectangle[1]:
            max_rectangle = curr_rectangle
            
    return max_rectangle
    