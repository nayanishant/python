""" 
    This program takes a list of words and a list of letters as input and find the words that can beformed using the letters.
    A character can't appear twice consecutively but can appear twice in the same word, i.e. Ball: wrong , Bomb : correct.
"""

def form_word(l1, l2):
    for i in l1:
        flag = 1
        for j in range(len(list(i)) - 1):
            if i[j] == i[j + 1]:
                flag = 0
            if i[j] not in l2:
                flag = 0
        if flag == 1:
            print(i)



words = ['log', 'blog', 'frog', 'seeker', 'bottle', 'spoon', 'mouse', 'key', 'bee', 'toss', 'craft', 'lift']
charset = ['o', 'g', 't', 'b', 'l', 'e', 'k', 'r', 'y', 'f']

form_word(words, charset)
