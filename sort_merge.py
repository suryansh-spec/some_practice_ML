def merge_sort(arr):

    if len(arr) <= 1:
        return arr
    

    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left,right)

def merge(left,right):
    result = []
    i = 0
    j = 0

    while i<len(left) and j<len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1 

        else:
            result.append(right[j])
            j += 1 

    result.extend(left[i:])
    result.extend(right[j:])
    return result

numbers = [54,84,9,545,87,4,54,65489,78,54,654,897,41,41657,897,5,132,1654]   
print(merge_sort(numbers))



    
