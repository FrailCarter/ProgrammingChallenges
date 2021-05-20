def mergesort(arr):

    def msort(low , high):
        # If our limits differ by 1, return that element of the array 
        # But! If they are less than 1, return nothing
        # Otherwise, recurse
        if high - low <= 1:
            yield from (arr[i] for i in range(low , high))
        else:
            mp = (high + low) // 2
            left = msort(low , mp)
            right = msort(mp , high)
            i , j = next(left) , next(right)
            while True:
                if i <= j:
                    yield i 
                    try:
                        i = next(left)
                    except StopIteration:
                        yield j 
                        break 
                else:
                    yield j
                    try:
                        j = next(right) 
                    except StopIteration:
                        yield i 
                        break 
            yield from left 
            yield from right 
    
    yield from msort(0 , len(arr))