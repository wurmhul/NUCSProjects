import random
import string

def generate_password(length=12):
    """Generates a random password.

    Args:
        length: The length of the password.

    Returns:
        A random password.
    """

    # Generate a random string of letters and numbers.
    password = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

    # Return the password.
    return password

def main():
    # Generate a random password.
    password = generate_password()

    # Print the results.
    print('Password: {}'.format(password))

if __name__ == '__main__':
    main()