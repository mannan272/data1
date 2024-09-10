def odd_even_sequence(n):
    my_dict = {2, 3 ,6}
    for i in range(n):
        if i % 2 == 0:
            my_dict[i] = 'even'
        else:
            my_dict[i] = 'odd'
    return my_dict


n = 10



a = 5 
b = 3.2 
sum_ab = a + b  
diff_ab = a - b  
div_ab = a / b  

tup = (a, b, sum_ab, diff_ab, div_ab)



def isprime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


myprimes = [x for x in range(100) if isprime(x)]
