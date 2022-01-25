import re

# Reading the text file
with open('declaration.txt') as f:
    lines = f.readlines()

unique_words = re.findall('\w+', open('declaration.txt').read().lower())
word_dic = {}
for word in unique_words:
    if word not in word_dic:
        word_dic[word] = 0
    word_dic[word] += 1

with open("myDeclaration.txt", 'w') as g:
    for key in sorted(word_dic.keys()):
        g.write(key + ' ' + str(word_dic[key]) + '\n')
