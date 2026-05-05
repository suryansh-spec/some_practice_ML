def quick_Sort(arr):
    
    if len(arr) <= 1:
        return arr


    pivot = arr[len(arr)//2]
    left = []
    equal= []
    right = []

    for x in arr:
        if x < pivot:
            left.append(x)

        elif x == pivot:
            equal.append(x)
        
        else:
            right.append(x)

    
    return quick_Sort(left) + equal + quick_Sort(right)

numbers = [648,79,41654,54,54,7,6,6,8,7,25132,18,77,97,564,5]
print(quick_Sort(numbers))

        
    
    

