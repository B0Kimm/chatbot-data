import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
baseurl = os.path.dirname(os.path.abspath(__file__))

import csv
import json
import glob
import re

input_file = r'C:\Users\USER\data\json\review(seoul)'

import pandas as pd
from pandas import DataFrame

shop_column = ['id', 'name', 'address','distance', 'lng','lat', 'delivery_fee','min_order_amount','open_time_description','review_avg','categories']
review_column = ['shopid', 'comment', 'rating', 'menu_summary', 'rating_quantity','rating_taste', 'rating_delivery', 'time', 'nickname', 'reviewid']
food_column = ['id', 'name', 'price', 'id', 'review_count']
chatbot_column = [ 'shopid', 'menu_summary', 'nickname', 'rating', 'customer_comment',  'owner_comment' ]

class YogiyoModel :
    def __init__(self, filename):
        self.filename = filename
        self.writer = None

    def hook_process(self) :
        yogiyo = YogiyoModel()
        self.yogiyo.convert()
        # self.yogiyo.get_seoul_data()
        # self.yogiyo.merge()

    def ngram(self):
        myframe = pd.read_csv(self.filename, sep = ',', encoding= 'utf-8')
        n = 2
        for index, row in myframe.iterrows():
            text = myframe['comment']
            result = []
            for a in range(len(text)-n + 1):
                result.append(text[a:a+n])
                return result
            

    def ngram_accu(aText, bText, num):
        aResult = ngram(aText,num)
        bResult = ngram(bText,num)
        cnt = 0
        r = []
        for i in aResult:
            for j in bResult:
                if i == j:
                    cnt += 1
                    r.append(i)
        return cnt/len(aResult), r

           

if __name__ == '__main__':
    filename = './csv/chatbot.csv'
    YogiyoModel(filename).ngram()


#word ngram
n = 2
result = []
mytext = list(text)
words = [mytext[x:x+n] for x in range(0, len(mytext))]

resultb = []
mytextb = list(textb)
words = [mytextb[x:x+n] for x in range(0, len(mytextb))]


cnt = 0
r = []
for i in result:
    for j in resultb:
        if i == j:
            cnt += 1
            r.append(i)
print(cnt/len(result))

def character_ngram(sentecen, n):
    ngrams=[]
    for a in range(len(text)-n + 1):
        result.append(text[a:a+n])
print(result)

def word_ngram(setence, n) :
    ngrams = []
    text = list(setence)
    ngrams = [text[x:x+n] for x in range(0, len(text))]

    return ngrams

def phoneme_ngram(setence, n):
    ngrams = []
    text = sentence.split(' ')
    ngrams = [text[x:x+n] for x in range(0, len(text))]

    return ngrams

