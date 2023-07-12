def key_positions(seq, key):
    """ key position function for a counting sort algorithm """
    #range of key values    
    key_length = max(key(a) for a in seq)+ 1
    #initialise the count array
    positions = [0] * key_length
    #generates the count array
    for a in seq:
        positions[key(a)] += 1
    #generates the key positions array
    sums = 0
    for j in range(key_length):
        positions[j], sums = sums, sums + positions[j]
    
    return positions


def sorted_array(seq, key, positions):
    """ Takes a sequence, a key function, and an array of positions generated by
        key_positions and produces an array (list) containing the elements of 
        seq sorted according to the key function.
    """
    sorted_arr = [None] * len(seq)
    for item in seq:
        sorted_arr[positions[key(item)]] = item
        positions[key(item)] += 1
    return sorted_arr


def radix_sort(numbers, d):
    """ Takes a sequence of natural numbers called numbers and uses counting 
        sort iteratively to sort the sequence up to the d-th digit from the 
        right. The argument d is a positive (and thus non-zero) integer.
    """
    numbers = list(numbers)

    for i in range(0,d):
        # modulo 10 grabs the rightmost number, and // 10**i brings the "grab" over 
        # i many numbers for every iteration in range(d)
        key = lambda x: (x // 10**i) % 10

        positions = key_positions(numbers, key)
        numbers = sorted_array(numbers, key, positions) 
    
    return numbers


# Test cases:
input_list = [329, 457, 657, 839, 436, 720, 355]
output_list = radix_sort(input_list, 3)
print(input_list)
print(output_list)
# Projected output
# [329, 457, 657, 839, 436, 720, 355]
# [329, 355, 436, 457, 657, 720, 839]

print(radix_sort([329, 457, 657, 839, 436, 720, 355], 1))
# Projected output
# [720, 355, 436, 457, 657, 329, 839]

print(radix_sort([329, 457, 657, 839, 436, 720, 355], 2))
# Projected output
# [720, 329, 436, 839, 355, 457, 657]