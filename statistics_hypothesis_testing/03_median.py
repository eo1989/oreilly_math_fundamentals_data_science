# Number of pets each person owns
sample = [0, 1, 5, 7, 9, 10, 14]

def median(values):
    ordered = sorted(values)
    print(ordered)
    n = len(ordered)
    mid = n // 2 - 1 if n % 2 == 0 else n // 2

    return (ordered[mid] + ordered[mid+1]) / 2.0 if n % 2 == 0 else ordered[mid]

print(median(sample)) # prints 5
