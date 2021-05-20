def fib_seq(stop):

    def build(x , y , step):
        while step <= stop:
            z = x + y 
            yield x
            x , y = y , z 
            step += 1 
    yield from build(0 , 1 , 0)
