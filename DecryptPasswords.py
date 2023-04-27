def scramble2Decrypt(cipherText):
  """Decrypts a ciphertext using the scramble2Encrypt function.

  Args:
    cipherText: The ciphertext to decrypt.

  Returns:
    The decrypted text.
  """

  # Check if the ciphertext is empty.
  if not cipherText:
    return ""

  # Get the length of the ciphertext.
  cipherTextLength = len(cipherText)

  # Get the half-length of the ciphertext.
  halfLength = cipherTextLength // 2

  # Get the even characters of the ciphertext.
  evenChars = cipherText[:halfLength]

  # Get the odd characters of the ciphertext.
  oddChars = cipherText[halfLength:]

  # Initialize the plaintext variable.
  plainText = ""

  # Iterate over the even and odd characters, alternating between them.
  for i in range(halfLength):
    plainText += evenChars[i]
    plainText += oddChars[i]

  # If there are more even characters than odd characters, append the last even character to the plaintext.
  if len(evenChars) > len(oddChars):
    plainText += evenChars[-1]

  # Return the plaintext.
  return plainText


def main():
  # Request user to input hashed password
  cipherText = input("Enter the cypherText password: ")

  # Decrypt the password.
  decrypted_password = scramble2Decrypt(cipherText)

  # Print the decrypted password.
  print(decrypted_password)


if __name__ == "__main__":
  main()