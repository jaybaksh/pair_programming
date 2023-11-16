# Following the flow 
    # Using stack traces, flow of execution, trying to follow line by line to where the issue is 
# Getting visibility
    # Printing out values around the line you tink the issue is on, to compare expected vs actual results 


def encode(text, key):
    #print(f"text: {text}")
    #print(f"key: {key}")
    cipher = make_cipher(key)
    #print(f"cipher: {cipher}")

    ciphertext_chars = []
    for i in text:
        #print("Loop starts again here")
        #print(f"i: {i}")
        # Research, what is chr() doing here? Whats its purpose? 
        #print(f"cipher.index(i): {cipher.index(i)}")
        ciphered_char = chr(65 + cipher.index(i))
        ciphertext_chars.append(ciphered_char)

    return "".join(ciphertext_chars)


def decode(encrypted, key):
    cipher = make_cipher(key)

    plaintext_chars = []
    for i in encrypted:
        plain_char = cipher[ord(i) - 65]
        print(f"plain_char: {plain_char}")
        print(f"ord i: {ord(i)}")
        plaintext_chars.append(plain_char)

    return "".join(plaintext_chars)


def make_cipher(key):
    #the alphabet was programmed incorrectly as the chr() function always starts a at 97 rather than 98. The range was incorrect as the index started at 1.
    alphabet = [chr(i + 97) for i in range(0, 26)]
    cipher_with_duplicates = list(key) + alphabet

    cipher = []
    #print(f"Alphabet: {alphabet}")
    for i in range(0, len(cipher_with_duplicates)):
        if cipher_with_duplicates[i] not in cipher_with_duplicates[:i]:
            cipher.append(cipher_with_duplicates[i])

    return cipher

# When you run this file, these next lines will show you the expected
# and actual outputs of the functions above.
print(f"""
 Running: encode("theswiftfoxjumpedoverthelazydog", "secretkey")
Expected: EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL
  Actual: {encode('theswiftfoxjumpedoverthelazydog', 'secretkey')}
""")

print(f"""
 Running: decode("EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL", "secretkey")
Expected: theswiftfoxjumpedoverthelazydog
  Actual: {decode('EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL', 'secretkey')}
""")
