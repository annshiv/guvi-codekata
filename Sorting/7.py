main_lst = list(map(int,input().strip()))
main_lst.sort()
for i in main_lst:
    if i != 0:
        main_lst.remove(i)
        main_lst.insert(0,i)
        break
main_word = ""
for i in main_lst:
    main_word += str(i)
print(main_word)