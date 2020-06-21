
def form_word():
    l1 = ['log', 'blog', 'frog', 'seeker', 'bottle', 'spoon', 'mouse', 'key', 'bee']
    l2 = ['o', 'g', 't', 'b', 'l', 'e', 'k', 'r', 'y', 'f']
    for i in l1:
        flag = 1
        for j in range(len(list(i)) - 1):
            if i[j] == i[j + 1]:
                flag = 0
            if i[j] not in l2:
                flag = 0
        if flag == 1:
            print(i)


form_word()