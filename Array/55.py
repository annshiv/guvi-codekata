n = input()
odd = ""
even = ""
for i in range(len(n)):
    if i % 2 == 0:
        even += n[i]
    else:
        odd += n[i]
print(even,odd)