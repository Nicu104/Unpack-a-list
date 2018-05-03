
#this method enters in a array and sum every single element
#using recursion

def unpack(x):
    sum = 0
    for i in x:
        if isinstance(i, list) or isinstance(i, tuple):
            sum += unpack(i)
        else:
            sum += i 
    return sum

#test case

print(unpack([1, 5, 6, [5, [5, 9, 1], 1], 8, 10, (5, 6)]))