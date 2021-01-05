n = input()
vowel = ['a','e','i','o','u']
word = ''
for i in n:
    if i not in vowel:
        word += i
if len(word) == 0:
    print(-1)
else:
    print(word[::-1])