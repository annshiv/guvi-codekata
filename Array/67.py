s = input()
word = ''
for i in s.strip():
    k = ord(i)+3
    if k == 91:
        word += chr(65)
    elif k == 92:
        word += chr(66)
    elif k == 93:
        word += chr(67)
    else:
        word += chr(k)
print(word)