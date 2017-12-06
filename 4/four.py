import data

def is_valid(passphrase):
    passphrase = passphrase.split(' ')
    unique = set()
    for word in passphrase:
        unique.add(word)
    return len(passphrase) == len(unique)

def is_valid_2(passphrase):
    passphrase = passphrase.split(' ')
    unique = set()
    for word in passphrase:
        letters = [letter for letter in word]
        letters.sort()
        unique.add(tuple(letters))
    return len(passphrase) == len(unique)

def count_valid(string, fn=is_valid):
    valid = 0
    for passphrase in string.split('\n'):
        if fn(passphrase):
            valid += 1
    return valid

assert count_valid(data.test_data) == 2
print('Task 1: data valid: {}'.format(count_valid(data.data)))

assert count_valid(data.test_data_2, fn=is_valid_2) == 3
print('Task 2: data valid: {}'.format(count_valid(data.data, fn=is_valid_2)))
