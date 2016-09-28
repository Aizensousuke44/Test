
def is_prime(num):   
    if num > 2:    
        flag = 0
        for n in range(2,num):
            if num % n == 0:
                flag += 1
        if flag > 1:            
            return False
        else:          
            return True
    elif num == 2:        
        return True
    else:       
        return False
