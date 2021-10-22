# GOLDBACHS CONJECTURE

def is_prime(number):
    if( number == 1 or number == 2):
        return True
    elif number <= 0:
        return False
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False
    return True

def goldbachs_conjecture(number, all_possibilities = False):
    if number < 2 or number % 2 != 0:
        return
    for i in range(1, number // 2 + 1):
        if (is_prime(i) and is_prime(number - i)):
            print(f"{i} + {number - i} = {number}")
            if not all_possibilities:
                return


# goldbachs_conjecture(20, all_possibilities = True)


# POLINDROME

def is_polindrome(x):
    if x < 10:
        return True
    digits = list(map(int, str(x)))
    for i in range(len(digits) // 2 + 1):
        if digits[i] != digits[-i - 1]:
            return False
    return True

def polindromes_in_range(a, b):
    for i in range(a, b):
        if(is_polindrome(i)):
            print(i, sep = " ")


# polindromes_in_range(13000, 13500)


# SUFFIX SUMS
# def suffix_sums():

# CYCLIC SHIFT

def cyclic_shift(digits, k):
    n = len(digits)
    k = k % n
    if k <= 0:
        return
    current_index = 0
    prev_node_val = digits[0]
    for _ in range(n):
        current_index += k
        current_index %= n
        curr_node_val = digits[current_index]
        digits[current_index] = prev_node_val
        prev_node_val = curr_node_val


#TREE

def asterisk_triangle(k):
    h = (k + 1) // 2
    # print(f"h = {h}")
    for i in range(h):

        for j in range(h - i - 1):
            print(" ", end="")

        for j in range(i*2 +1):
            print("*", end="")
        print("")


def suffix_sums(array):
    b = [0] * len(array)
    c = 0
    print(f"length of b is {len(b)}")
    for i in range(len(array)):
        c += array[len(array) - 1 - i]
        b[len(array) - 1 - i] = c
    print(b)
