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

    def only_string(self) :
        myframe = pd.read_csv(self.filename, sep = ',', encoding= 'utf-8')

        myframe['customer_comment'] = myframe['customer_comment'].replace('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', ' ', regex=True)
        myframe['owner_comment'] =  myframe['owner_comment'].replace('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', ' ', regex=True)
        print(myframe.head(100))

        emoji = re.compile("[" u"\U00010000-\U0010FFFF" "]+", flags=re.UNICODE)
        myframe['customer_comment'] = emoji.sub(r'', str(myframe['customer_comment']))
        

        # myframe.astype(str).apply(lambda x: x.str.encode('ascii', 'ignore').str.decode('ascii'))
        # myframe.astype(str).apply(lambda x: x.str.encode('utf-8', 'ignore').str.decode('utf-8'))
        
        # print(myframe.head(100))
        # myframe['customer_comment'] = myframe['customer_comment'].str.encode('utf-8', 'ignore').str.decode('utf-8')
        # myframe['owner_comment'] =  myframe['owner_comment'].str.encode('utf-8', 'ignore').str.decode('utf-8')

        # print(myframe.head(100))
    #     return data.encode('utf-8', 'ignore').decode('utf-8')
        
        # emoji = re.compile("[" u"\U00010000-\U0010FFFF" "]+", flags=re.UNICODE)
        # myframe['customer_comment'] = emoji.sub(r'', str(myframe['customer_comment']))

        # myframe['customer_comment'] = myframe['customer_comment'].str.encode('utf-8', 'ignore').str.decode('utf-8')
        # myframe['owner_comment'] =  myframe['owner_comment'].str.encode('utf-8', 'ignore').str.decode('utf-8')
        
        outputname = f'{self.filename}.csv'
        myframe.to_csv(outputname, mode='w', encoding='utf-8', index=False)

        print('------------ finished --------')

    def ngram_comparison(self, text, n):
        result = []
        for a in range(len(text)-n + 1):
            result.append(text[a:a+i])
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

           
    def review_csv(self) :
        # CSV_COLUMNS=[storeid, comment, rating, menu_summary, rating_quantity, rating_taste, rating_delivery, time, nickname,customerid]
        with open(self.filename, 'rb') as json_file:
            data = json.load(json_file)
            result = []
            for item in data:
                if item['id'] != '':
                    id = item['id']
                    reviews = item['reviews']
                    for idx in reviews:
                        comment = idx['comment']
                        comment = comment.replace('\r', '')
                        comment = comment.replace('\n', '')
                        imsi = [ item['id'], comment, idx['rating'], idx['menu_summary'], idx['rating_quantity'], idx['rating_taste'], idx['rating_delivery'], idx['time'], idx['nickname'], idx['id'] ]
                        result.append(imsi)
                else:
                    id = ''   
            
        result = pd.DataFrame(result, columns=review_column)
        outputname = f'{self.filename}.csv'
        result.to_csv(outputname, mode='w', encoding='utf-8', index=False)

        print('------------ finished --------')

    def chatbot_csv(self) :
        # CSV_COLUMNS=[storeid, comment, rating, menu_summary, rating_quantity, rating_taste, rating_delivery, time, nickname,customerid]
        with open(self.filename, 'rb') as json_file:
            data = json.load(json_file)
            result = []
            for item in data:
                if item['id'] != '':
                    id = item['id']
                    reviews = item['reviews']
                    for idx in reviews:
                        comment = idx['comment']
                        comment = comment.replace('\r', '')
                        comment = comment.replace('\n', '')
                        reply = idx['owner_reply']
                        if reply != None :
                            owner_comment = reply['comment']
                            owner_comment = owner_comment.replace('\r', '')
                            owner_comment = owner_comment.replace('\n', '')
                            imsi = [ item['id'], idx['menu_summary'], idx['rating'], idx['nickname'],  comment,  owner_comment ]
                            result.append(imsi)                          
           
        result = pd.DataFrame(result, columns=chatbot_column)
        outputname = f'{self.filename}.csv'
        result.to_csv(outputname, mode='w', encoding='utf-8', index=False)

        print('------------ finished --------')

    def menu_csv(self):         
        with open(self.filename, 'rb') as json_file:
            data = json.load(json_file)
            result = []
            for item in data:
                id = item['id']
                menus = item['menus']
                for idx in menus:
                    imsi = [ item['id'], idx['name'], idx['price'], idx['id'], idx['review_count'] ]
                    result.append(imsi)          
            
        result = pd.DataFrame(result, columns=menu_column)
        outputname = f'{self.filename}.csv'
        result.to_csv(outputname, mode='w', encoding='utf-8', index=False)

        print('------------ finished --------')


    def merge(self) :
        data = []
        for file in allFile_list :
            df = pd.read_csv(file)
            data.append(df)
            dataCombine = pd.concat(data, axis=0, ignore_index=True)

        output_file = r'C:\Users\USER\data\csv\review.csv'
        dataCombine.to_csv(output_file, index=False)

        print(f'---------------csv created ---------------')

    def preprocessing(self) :
        filename = '.\csv\seoul.csv'
        myframe = pd.read_csv(self.filename, sep = ',', encoding= 'utf-8')

        myframe = myframe.dropna(axis=0)
        
        csvfilename = 'seoul_store_info.csv'
        myframe.to_csv(csvfilename, mode= 'w', encoding='utf-8',index=False)
        print(f'--------{csvfilename} done -------------')

if __name__ == '__main__':
    filename = './csv/chatbot.csv'
    YogiyoModel(filename).only_string()

# for 
#              text = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', '', data)
#             return 
#         print()
