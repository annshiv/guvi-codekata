n = input()
count = 0
for i in n:
    try:
        count += int(i)
    except ValueError:
        pass

print(count)