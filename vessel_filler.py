def vessel_filler(time , vessel_size , rate):

    def fill(t , rate , level , vessels):
        amount = 0
        ticks = 0
        while t < time:
            while ticks * rate < vessel_size:
                ticks += 1 
                t += 1
                amount = ticks * rate 
            if t <= time:
                rate /= 2
                level += 1
                vessels *= 2
                # This means the vessels have filled
                return fill(t , rate , level , vessels)
            else:
                vessels //= 2 
                break 
        return vessels 
    return "Vessels filled: {0}".format(fill(0 , rate , 0 , 1))