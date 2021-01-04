s = input()
word = ''
if len(s) % 2 ==0:
    for i in range(1,len(s),2):
        word += s[i]
        word += s[i-1]
else:
    for i in range(1,len(s)-1,2):
        word += s[i]
        word += s[i-1]
    word += s[-1]

print(word)