lowers = range(ord('a'), ord('z')+1)

def cipher(string):
    encrypted = []
    for c in string:
        code = ord(c)
        if code in lowers:
            encrypted_code = 219 - code
            encrypted_char = chr(encrypted_code)
        else:
            encrypted_char = c
        encrypted.append(encrypted_char)

    return ''.join(encrypted)



print(cipher(cipher('This is a [good] example.')))
