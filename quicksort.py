def quicksort(arr):

    def qsort(low , high):
        if low >= high:
            return 
        
        i , j = low , high 
        pivot = arr[random.randint(low , high)]

        while i <= j:
            while arr[i] < pivot:
                i += 1
            
            while arr[j] > pivot:
                j -= 1 
            
            if i <= j:
                arr[i] , arr[j] = arr[j] , arr[i]
                i += 1
                j -= 1
        qsort(low , j)
        qsort(i , high)
    
    qsort(0 , len(arr) - 1)
    return arr 
# When we do this with cards, I can say that when i == j, the pivot either goes to the left or right of that spot (depending on 
# if the index is at the beginning or end of the list, respectively.
# However, since I am not popping off the pivot in the list, and I am not slicing the list either, that means that 
# once i == j, we hit an infinite loop, since one of the sides will never get any smaller

# To get around this, we allow i and j to cross. This means that that spot where they were equal will be excluded.
# For example, if our i, j were 7, 7, and the length of the list is 8, then i, j become 8, 6. Our next call to qsort
# would be for (0 , 6) and (8 , 7). This cuts out the right side properly, and shortens the left side by 1, which is like
# what pop would do for the pivot 