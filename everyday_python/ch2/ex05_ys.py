# 피그라틴 단어 만들기

def make_piglatin(word):
    if word[0] in 'a,e,i,o,u':
        print(f'{word}way') 
    else:
        print(f'{word[1:]}{word[0]}ay')

input_word = input('Please write a word: ')
make_piglatin(input_word)