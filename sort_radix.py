def radix_sort(arr):
    if len(arr) == 0:
        return arr
    
    max_num = max(arr)
    
    place = 1
    
    while max_num // place > 0:
        arr = counting_sort_by_digit(arr, place)
        place *= 10
    
    return arr


def counting_sort_by_digit(arr, place):
    buckets = [[] for _ in range(10)]
    
    for num in arr:
        digit = (num // place) % 10
        buckets[digit].append(num)
    
    result = []
    for bucket in buckets:
        result.extend(bucket)
    
    return result

numbers = [5489,74,1,564,8,7487,54,7,5487,11,57,89714,5,79,87,4,165,464,64,97,765,41]
print(radix_sort(numbers))
