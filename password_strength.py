import re
import getpass


def get_length_strength(password):
    good_length = 10
    normal_length = 8
    bad_length = 5
    if len(password) > good_length:
        return 3
    elif len(password) > normal_length:
        return 2
    elif len(password) > bad_length:
        return 1
    else:
        return 0


def get_character_diversity(password):
    counter = 0
    array_patterns_to_check = ['[a-z]', '[A-Z]', '\d', '\W']
    for pattern in array_patterns_to_check:
        match = re.search(pattern, password)
        if match:
            counter += 1
    return counter


def get_password_strength(password):
    strength_length = get_length_strength(password)
    strength_diversity = get_character_diversity(password)
    total_strength = sum((strength_length, strength_diversity))
    return total_strength


def main():
    password = getpass.getpass('Input password to check: ')
    print('{}: {}'.format('Strength of your password', get_password_strength(password)))


if __name__ == '__main__':
    main()
