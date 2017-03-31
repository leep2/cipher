def cipher(text, cipher_alphabet, option='encipher'):
    ciphered = ''
    if option == 'encipher':
        for c in text:
            if c == ' ':
                ciphered += ' '
            else:
                ciphered += cipher_alphabet[c]
    elif option == 'decipher':
        reverse_cipher_alphabet = dict(zip(cipher_alphabet.values(), cipher_alphabet.keys()))
        for c in text:
            if c == ' ':
                ciphered += ' '
            else:
                ciphered += reverse_cipher_alphabet[c]
    return ciphered