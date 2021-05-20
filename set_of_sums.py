def sum_items(*items): 
    res = 0 
    for item in items: 
        res += item 
    return res 
  
def make_sorted_tuple(*items): 
    res = tuple(sorted([i for i in items]))
    return res 

  
def sum_to_k(list_of_ints , k): 
    s = dict() 
    less_than = set()
    m = len(list_of_ints) 
      
    def get_sums(i , less_than): 
        l = set()
        e = set() 
        if i == 1: 
            for x in list_of_ints: 
                if x < k: 
                    l.add(make_sorted_tuple(x))
                elif x == k: 
                    #print(x)
                    e.add(make_sorted_tuple(x))
                else: 
                    continue 
            s[i] = e 
            return l 
        else: 
            for x in less_than: 
                y = [j for j in list_of_ints if j not in x] 
                for n in y: 
                    if sum_items(n , *x) < k: 
                        l.add(make_sorted_tuple(n , *x))
                    elif sum_items(n , *x) == k: 
                        #print(n , x)
                        e.add(make_sorted_tuple(n , *x))
                    else: 
                        continue 
            s[i] = e 
            return l
            
    for i in range(1 , m + 1): 
        less_than = get_sums(i , less_than) 
    return s
  
      
  
a = sum_to_k([5 , 10 , 11 , 12 , 13 , 15 , 18 , 25] , 30)  
b = sum_to_k([5 , 10 , 11 , 12 , 13 , 15 , 18 , 25] , 40)
c = sum_to_k([1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10] , 20)  
d = sum_to_k([1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10] , 50) 
e = sum_to_k([i for i in range(1 , 51)] , 100)  
# Slow, losing time ordering tuples, repeat loops
# First pass solution is done 



