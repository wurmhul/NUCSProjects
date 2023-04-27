import PasswordGenerator

def plainText():
    password = PasswordGenerator.generate_password()
    return password

def scramble2Encrypt(plainText):
    evenChars = ""
    oddChars = ""
    charCount = 0
    for ch in plainText:
        if charCount % 2 == 0:
            evenChars = evenChars + ch
        else:
            oddChars = oddChars + ch
        charCount = charCount + 1
        cipherText = oddChars + evenChars
        print (cipherText)

# Generate a password
password = plainText()

# Encrypt the password
encrypted_password = scramble2Encrypt(password)

# Print the full encrypted password
print (encrypted_password, end="")


