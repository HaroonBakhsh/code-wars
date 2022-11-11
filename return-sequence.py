# Build a function that returns an array of integers from n to 1 where n>0.
#
# Example : n=5 --> [5,4,3,2,1]

def reverse_seq(n):
    sequence = []
    for number in range(1, n+1):
        sequence.append(number)
    return sequence[::-1]


print(reverse_seq(5))


# alternative better solution

def rev_seq(n):
    return list(range(n, 0, -1))


print(rev_seq(5))
