def fizzbuzz(x):

    if (x % 3 == 0) and (x % 5 == 0):
        q = 'FizzBuzz'
    else:
        if x % 3 == 0:
            q = 'Fizz'
        if x % 5 == 0:
            q = 'Buzz'
        if (x % 3 != 0) and (x % 5 != 0):
            q = x

    return q
                
                


        
