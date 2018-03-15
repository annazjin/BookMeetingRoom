# -*- coding: utf-8 -*-
import sys
import nltk
reload(sys)
sys.setdefaultencoding('utf-8')
article= open('article.txt').read()
tokens=nltk.word_tokenize(article)
t=nltk.text.Text(tokens)#构造使用nltk.text.Text()类用于文本统计分析的对象
print t.concordance('language')
print "#####################################################################################################"
fdist = nltk.FreqDist(tokens)
#fdist.tabulate(20, cumulative=True)
wordlist=fdist.keys()[:50]
print wordlist