# from haversine import haversine, Unit
import pandas as pd
from pandas import DataFrame
import csv


review = './csv/review.csv'
food = './csv/menu.csv'
store = './csv/store.csv'
test ='test.csv'
test2 ='test2.csv'
test3 ='test3.csv'

myreview = pd.read_csv(review, sep = ',', encoding= 'utf-8')
myfood = pd.read_csv(food, sep = ',', encoding= 'utf-8')
mystore = pd.read_csv(store, sep = ',', encoding= 'utf-8')
mytest = pd.read_csv(test, sep = ',', encoding= 'utf-8')
mytest2 = pd.read_csv(test2, sep = ',', encoding= 'utf-8')
mytest3 = pd.read_csv(test3, sep = ',', encoding= 'utf-8')

# print(myreview.columns) #Index(['shopid', 'comment', 'rating', 'menu_summary', 'rating_quantity', 'rating_taste', 'rating_delivery', 'time', 'nickname', 'reviewid'])
# print(myfood.columns)
# print(mystore.columns)
# print(mytest.columns)
# print(mytest2.columns)
# print(mytest3.columns) #Index(['id', 'name', 'address', 'distance', 'lat', 'lng', '시', '구', '동', '지번', '상세', 'nickname', 'orderid', 'menu_summary', 'comment'],

column1s = ['shopid','nickname','reviewid', 'time', 'menu_summary','comment']
column2s = ['shopid','name','lat','lng','address', '구', '동','지번']
columns = ['shopid','name','lat','lng','address', '동','지번','nickname','reviewid','reviewtime', 'menu_summary','comment']
column3s = ['orderid', 'time']

# id,name,lat,lng,address,동,지번,nickname,orderid,menu_summary,comment
# # row에서 필요한 셀만 추가 (review)
# result = []
# for index, row in myreview.iterrows():
#     imsi = [row['reviewid'],row['time']]
#     result.append(imsi)    

# result = pd.DataFrame(result, columns=column3s)
# result.to_csv('time.csv', mode='w', encoding='utf-8', index=False)

gangnam ='gangnam.csv'
seocho ='seocho.csv'
time = 'time.csv'

mygangnam = pd.read_csv(gangnam, sep = ',', encoding= 'utf-8')
myseocho = pd.read_csv(seocho, sep = ',', encoding= 'utf-8')
mytime = pd.read_csv(time, sep = ',', encoding= 'utf-8')

mergegangnam = pd.merge(mygangnam, mytime, on='orderid', how='left')
mergegangnam.to_csv('gangnam.csv', mode='w', encoding='utf-8', index=False)

merseocho = pd.merge(myseocho, mytime, on='orderid', how='left')
merseocho.to_csv('seocho.csv', mode='w', encoding='utf-8', index=False)

# # test에서 필요한 셀만 추가(test3)
# outcome = []
# for index, row in mytest3.iterrows():
#     imsi = [row['id'], row['name'],row['lat'],row['lng'], row['address'],row['구'], row['동'], row['지번'] ]
#     outcome.append(imsi)    
# outcome = pd.DataFrame(outcome, columns=column2s)
# outcome.to_csv('outcome.csv', mode='w', encoding='utf-8', index=False)

# outcome ='outcome.csv'
# result ='result.csv'

# myoutcome = pd.read_csv(outcome, sep = ',', encoding= 'utf-8')
# myresult = pd.read_csv(result, sep = ',', encoding= 'utf-8')

# mergedata = pd.merge(myresult, myoutcome, on='shopid', how='left')
# mergedata.to_csv('mergedata.csv', mode='w', encoding='utf-8', index=False)

# final = []
# for index, row in myoutcome.iterrows():
#     if row['구'] == '강남구' :
#         # comment = row['comment']
#         # comment = comment.replace('\r', ' ')
#         # comment = comment.replace('\n', ' ')
#         imsi = [row['id'], row['name'],row['lat'],row['lng'], row['address'],row['구'], row['동'], row['지번'] ]
#         # imsi = [row['id'], row['name'], row['lat'],row['lng'], row['address'], row['동'], row['지번'], row['nickname'],row['reviewid'],row['time'], row['menu_summary'],comment ]
#         final.append(imsi)

# final = pd.DataFrame(final, columns=column2s)
# final.to_csv('outcome.csv', mode='w', encoding='utf-8', index=False)

# final2 = []
# for index, row in mergedata.iterrows():
#     if row['구'] == '서초구' :
#         comment = row['comment']
#         # comment = comment.replace('\r', ' ')
#         # comment = comment.replace('\n', ' ')
#         imsi = [row['id'], row['name'], row['lat'],row['lng'], row['address'], row['동'], row['지번'], row['nickname'],row['reviewid'],row['time'], row['menu_summary'],comment ]
#         final.append(imsi)

# final2 = pd.DataFrame(final2, columns=columns)
# final2.to_csv('seocho.csv', mode='w', encoding='utf-8', index=False)

# row에서 필요한 셀만 추가
# result = []
# for index, row in myframe.iterrows():
#     if row['구'] == '강남구' :
#         comment = row['comment']
#         # comment = comment.replace('\r', ' ')
#         # comment = comment.replace('\n', ' ')
#         imsi = [row['id'], row['name'], row['lat'],row['lng'], row['address'], row['동'], row['지번'], row['nickname'],row['orderid'],row['menu_summary'],comment ]
#         result.append(imsi)

# result = pd.DataFrame(result, columns=columns)
# result.to_csv('gangnam.csv', mode='w', encoding='utf-8', index=False)


# class YogiyoModel :
#     def __init__(self, filename):
#         self.filename = filename
#         self.writer = None

#      def

#     def chatbot_csv(self) :
#             # CSV_COLUMNS=[storeid, comment, rating, menu_summary, rating_quantity, rating_taste, rating_delivery, time, nickname,customerid]
#             with open(self.filename, 'rb') as json_file:
#                 data = json.load(json_file)
#                 result = []
#                 for item in data:
#                     if item['id'] != '':
#                         id = item['id']
#                         reviews = item['reviews']
#                         for idx in reviews:
#                             comment = idx['comment']
#                             comment = comment.replace('\n', ' ')
#                             reply = idx['owner_reply']
#                             if reply != None :
#                                 imsi = [ item['id'], idx['menu_summary'], idx['nickname'], idx['rating'], comment,  reply['comment'] ]
#                                 result.append(imsi)                          
#             result = pd.DataFrame(result, columns=testcolums)
#             outputname = f'{self.filename}.csv'
#             result.to_csv(outputname, mode='w', encoding='utf-8', index=False)

#             print('------------ finished --------')

# if __name__ == '__main__':
#     YogiyoModel()