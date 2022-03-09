# Imports
import itertools
import time



# Brute force function
def brute_force(secret_password):
    start = time.time()
    chars = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`~!@#$%^&*()_-+=[{]}|:;'\",<.>/?"
    attempts = 0
    for num in range(int(len(secret_password) + 1)):
        for letter in itertools.product(chars, repeat=num): #.product: nested loops cycle, same as ((x,y) for x in A for y in B)
            attempts += 1
            letter = ''.join(letter)
            if letter == secret_password: # Breaks out of the for loop if secret matches loop attempts
                end = time.time()
                distance = end - start
                return (letter, attempts, round(distance, 2))

