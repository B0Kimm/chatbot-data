import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
baseurl = os.path.dirname(os.path.abspath(__file__))


import csv
import json
import glob
import re

input_file = r'C:\Users\USER\prep_data\json\review(seoul)'
# input_file = r'C:\Users\USER\prep_data\raw'

import pandas as pd
from pandas import DataFrame

shop_column = ['id', 'name', 'address','distance', 'lng','lat', 'delivery_fee','min_order_amount','open_time_description','review_avg','categories']
review_column = ['shopid', 'comment', 'rating', 'menu_summary', 'rating_quantity','rating_taste', 'rating_delivery', 'time', 'nickname', 'reviewid']
food_column = ['id', 'name', 'price', 'id', 'review_count']
chatbot_column = [ 'shopid', 'menu_summary', 'nickname', 'rating', 'customer_comment',  'owner_comment' ]
owner_column = ['orderid', 'owner_comment']
movie_column = ['review']
review_sent_column = ['review', 'point']

class YogiyoModel :
    def __init__(self, filename):
        self.filename = filename
        self.writer = None

    def hook_process(self) :
        yogiyo = YogiyoModel()
        self.yogiyo.convert()
        # self.yogiyo.get_seoul_data()
        # self.yogiyo.merge()

    def _process(self, item):
        if item['city'] == '서울' :  
            id = item['id']
            name = item['name']
            address = item['address']
            categories = item['categories']
            distance = item['distance']
            lat = item['lat']
            delivery_fee = item['delivery_fee']
            min_order_amount = item['min_order_amount']
            open_time_description = item['open_time_description']
            lng = item['lng']
            review_avg = item['review_avg']
        else :
            id = ''
            name = ''
            address = ''
            categories = ''
            distance = ''
            lat = ''
            delivery_fee = ''
            min_order_amount = ''
            open_time_description = ''
            lng = ''
            review_avg = ''
        return [id, name, address, distance, lng, lat, delivery_fee, min_order_amount, open_time_description, review_avg, categories]
  
    def convert(self):
        with open(self.filename, 'rb') as json_file:
            data = json.load(json_file)
            with open(self.filename + '.csv', 'wt', newline='',encoding="UTF-8-SIG") as csv_file:
                self.writer = csv.writer(csv_file, delimiter=',')
                self.writer.writerow(CSV_COLUMNS)
                for item in data:
                    row = self._process(item)
                    self.writer.writerow(row)
            print('----finished----')

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
                        imsi = [comment, idx['rating']]
                        # reply = idx['owner_reply']
                        # if reply != None :
                        #     owner_comment = reply['comment']
                            # owner_comment = owner_comment.replace('\r', '')
                            # owner_comment = owner_comment.replace('\n', '')
                            # imsi = [comment, idx['rating']]
                        result.append(imsi)                          
           
        result = pd.DataFrame(result, columns=review_sent_column)
        outputname = f'{self.filename}.csv'
        result.to_csv(outputname, mode='w', encoding='utf-8', index=False)

        print('------------ finished --------')

    def movie_review(self):
        with open(self.filename, 'rb') as json_file:
            data = json.load(json_file)
            result = []
            for item in data:
                imsi = [ item['review'] ]
                result.append(imsi)                          
           
        result = pd.DataFrame(result, columns=movie_column)
        outputname = f'{self.filename}.csv'
        result.to_csv(outputname, mode='w', encoding='utf-8', index=False)

        print('------------ finished --------')

    def owner_csv(self) :
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
                            imsi = [ idx['id'], idx['comment'] ]
                            result.append(imsi)                          
           
        result = pd.DataFrame(result, columns=owner_column)
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

        output_file = r'C:\Users\USER\prep_data\csv\sent_review.csv'
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
    # filename = '.\csv\review.csv'
    # YogiyoModel(filename).owner_csv()
    allFile_list = glob.glob(os.path.join(input_file, 'yogiyo_review(*' +'.csv'))
    
    for file in allFile_list :
            YogiyoModel(f'{file}').merge()
    # filename = '.\csv\seoul.csv'