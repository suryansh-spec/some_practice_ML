def selection_sort(arr):

    for current_pos in range(len(arr)):
        smallest_pos = current_pos


        for checking_pos in range(current_pos + 1, len(arr)):
            if arr[checking_pos] < arr[smallest_pos]:
                smallest_pos = checking_pos

        
        arr[current_pos], arr[smallest_pos] = (arr[smallest_pos], arr[current_pos])
        

    return arr

numbers = [10,5,9,7,5,3,2,48,5,2,5]
print(selection_sort(numbers))

