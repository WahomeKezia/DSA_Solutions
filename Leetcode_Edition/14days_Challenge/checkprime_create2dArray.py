
"""
Create a two dimensional array of integers numbers and find out largest prime number among all diagonal elements.
E.G of 2-d array are below
1 2 3 4
4 3 2 1
7 8 9 6
13 5 4 3

Princiapl Diagonal 1,3,9,3
Secondary Diagonal 4,2,8,13
"""
# A function to check if prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**(0.5)) + 1):
        if num % i == 0:
            return False
    return True
# create the 2d array
def largest_prime_diagonal(arr):
    ''' declaring my variables n,m, prime_list
     a 2d arr is (n*m)'''

    # m is th column
    m = len(arr)
    # n is the row
    n = len(arr[0])

    prime_list = []
    for i in range(m):
        for j in range(n):
            if i == j: # principal diagonal
                if is_prime(arr[i][j]):
                    prime_list.append(arr[i][j])
            if i + j == m - 1: # secondary diagonal
                if is_prime(arr[i][j]):
                    prime_list.append(arr[i][j])
    return max(prime_list) if prime_list else None


array = [[1, 2, 3, 4], [4, 3, 2, 1], [7, 8, 9, 6], [13, 5, 4, 3]]
print(largest_prime_diagonal(array)) # Output: 13