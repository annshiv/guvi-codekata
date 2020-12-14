n = int(input())
att_lst = list(map(str,input().split(" ")))
present = 0
for i in att_lst:
    if i == "P":
        present += 1
attendance = (present / n) * 100
if attendance <= 25:
    print("Blacklisted")
else:
    print("Not Blacklisted")