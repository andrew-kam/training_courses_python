from simplecrypt import decrypt  # encrypt

with open("encrypted.bin", "rb") as inp:
    encrypted = inp.read()
# password = 'RVrF2qdMpoq6Lib'

with open('passwords.txt') as inf:
    for line in inf:
        password = line.strip()
        try:
            laintext = decrypt(password, encrypted)
            print(password)
            print(laintext)
            break
        except:
            pass
