'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    th = "th"

    if word.find(th) != -1:
        new_th = word.replace(th, " ", 1)
        print(new_th)
        return 1 + count_th(new_th)
    else:
        return 0

count_th('thathth')