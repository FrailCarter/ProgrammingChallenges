def binary_search(sorted_arr , element):

    def search(low , high):
        if low >= high:
            return
        
        rng = [i for i in range(low , high + 1)]
        midpt = rng[len(rng) // 2]
        if sorted_arr[midpt] > element:
            high = midpt
        elif sorted_arr[midpt] < element:
            low = midpt 
        else:
            return midpt
        return search(low , high)
    
    return search(0 , len(sorted_arr) - 1)
