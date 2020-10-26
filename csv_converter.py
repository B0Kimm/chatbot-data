import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
baseurl = os.path.dirname(os.path.abspath(__file__))

import csv
import json
import glob

input_file = r'C:\Users\USER\data'

import pandas as pd

CSV_COLUMNS = ['id', 'comment']

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
        id = item['id']
        reviews = item['reviews']
        reviews1 = item.get('reviews', [])
        comment = 
        return [id, name, address,distance, lng,lat, delivery_fee,min_order_amount,open_time_description,review_avg,categories]

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

    def merge(self) :
        data = []
        for file in allFile_list :
            df = pd.read_csv(file)
            data.append(df)
        dataCombine = pd.concat(data, axis=0, ignore_index=True)

        output_file = r'C:\Users\USER\chatbot-order\chatbot-order-api\csv\seoul.csv'
        dataCombine.to_csv(output_file, index=False)

        print('---------------csv created---------------')

    def preprocessing(self) :
        filename = '.\csv\seoul.csv'
        myframe = pd.read_csv(self.filename, sep = ',', encoding= 'utf-8')

        myframe = myframe.dropna(axis=0)
        
        csvfilename = 'seoul_store_info.csv'
        myframe.to_csv(csvfilename, mode= 'w', encoding='utf-8',index=False)
        print(f'--------{csvfilename} done -------------')

if __name__ == '__main__':
    allFile_list = glob.glob(os.path.join(input_file, 'yogiyo_review*'+'.json'))
    
    for file in allFile_list :
            for file in allFile_list :
                YogiyoModel(f'{file}').convert()
    # filename = '.\csv\seoul.csv'