import sys
import nltk
reload(sys)
sys.setdefaultencoding('utf-8')
#article= open('article.txt').read()
#tokens=nltk.word_tokenize(article)

limit=50
file_count=0
word_list=[]

with open("resume.txt") as f:
    fr=f.read()
    tokens=nltk.word_tokenize(fr)
    
    for token in tokens:
    
        word_list.append(" "+token)
        if len(word_list)<limit:
            continue
        file_name=str(file_count)+".txt"
        with open(file_name,'w') as file:
            for word in word_list[:-1]:
                file.write(word)
            file.write(word_list[-1].strip())
            word_list=[]
            file_count+=1
if word_list:
    file_name=str(file_count)+".txt"
    with open(file_name,'w') as file:
        for word in word_list:
            file.write(word)
print('done')
