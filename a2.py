#
# The code contains functions to solve the Syracuse problem: operations applied to positive integer values 
# once or iteratively to generate a sequence until a stopping condition is reached.
# ANTONIETTA SAGGESE 119112807 - 13th OCTOBER 2019
#

def syracuse_fn(n):
    # Calculate the Syracuse operation on the argument of the parameter n and
    # return the result of the calculation (result): if n is even the number is
    # divided by 2, if it's odd the number is multiplied by three and added to one
    if n%2==0:
        result=n//2
    else:
        result=n*3+1
    return result


def syracuse_seq(n):
    # Compute the Syracuse sequence from the argument of the parameter n as starting point and return 
    # the length of the sequence (length) and the value of largest element in the sequence (maximum)
    
    MAX_LEN=1000                              # define MAX_LEN as the maximum value of the sequence length    
    length=1                                  # initializationof the sequence length to one
                                              # e.g if n==1, the sequence will have length 1

    maximum=n


    for j in range (MAX_LEN):                 # for loop considering a length of the sequence of maximum 1000 elements
        
        result=syracuse_fn(n)
        n=result                            
        length=length+1
        if result> maximum:
            maximum=result
        if result==1:
            break
    return length, maximum


def longest_seq(n):
    # Compute the Syracuse sequence having as starting point the numbers up to and including n and
    # return the starting point of the longest sequence (start_max) and its length (longest)
    
    longest=0
    start_max=n
    for i in range (n,0,-1):
        length,maximum = syracuse_seq(i)
        if length>longest:
            longest = length
            start_max=i
    return start_max, longest







