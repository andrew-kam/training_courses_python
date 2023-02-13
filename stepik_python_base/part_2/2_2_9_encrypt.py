from simplecrypt import decrypt

with open("2_2_9_encrypted.bin", "rb") as inp:
    encrypted = inp.read()
# password = 'RVrF2qdMpoq6Lib'

with open('2_2_9_passwords.txt') as inf:
    for line in inf:
        password = line.strip()
        try:
            line_text = decrypt(password, encrypted)
            print(password)
            print(line_text)
            break
        except:
            pass

# https://stepik.org/lesson/24466/step/9?unit=6773
