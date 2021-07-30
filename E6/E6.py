def sum_of_squares(n):
    sum = int((n*(n+1)*(2*n+1))/6)
    return sum

def square_of_sum(n):
    sum = int((n*(n+1))/2)
    square = sum * sum
    return square

difference = square_of_sum(100) - sum_of_squares(100)
print(difference)