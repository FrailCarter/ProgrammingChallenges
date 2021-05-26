def get_all_sums(a , b):
    
    def retrieve_items(*items):
        return [a[i] for i in items]

    def build(lt , s):
        pos = lt[-1] + 1
        if a[pos:] == []:
            return 
        else:
            while pos < len(a):
                if s + a[pos] < b:
                    yield from build(lt + [pos] , s + a[pos])
                    pos += 1
                elif s + a[pos] == b:
                    yield retrieve_items(*lt , pos)
                    pos += 1 
                else:
                    pos += 1

    for i in range(0 , len(a)):
        # index of each singular element in the list
        if a[i] < b:
            yield from build([i] , a[i])
        elif a[i] == b:
            yield a[i]
        else:
            continue
  
      
  
a = sum_to_k([5 , 10 , 11 , 12 , 13 , 15 , 18 , 25] , 30)  
b = sum_to_k([5 , 10 , 11 , 12 , 13 , 15 , 18 , 25] , 40)
c = sum_to_k([1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10] , 20)  
d = sum_to_k([1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10] , 50) 
e = sum_to_k([i for i in range(1 , 51)] , 100)  
# Slow, losing time ordering tuples, repeat loops
# First pass solution is done 



