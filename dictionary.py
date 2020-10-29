import re
import csv
import pandas as pd
from pandas import DataFrame

# # shop = 'store.csv'
# review = './data/sent_review.csv'
food = './data/food.csv'

# # df = pd.read_csv(shop, sep = ',', encoding= 'utf-8' )
# df1 = pd.read_csv(review, sep=',', encoding='utf-8')
# df2 = pd.read_csv('./data/review_sen.csv', sep = ',', encoding= 'utf-8')
df3 = pd.read_csv(food, sep = ',', encoding= 'utf-8')
# input_file = './data/review.txt'


# # sentiment analysis 데이터 만들기
# sent_column = ['review', 'point']
# # result = []
# # for index, row in df1.iterrows():
# #     comment = row['customer_comment']
# #     imsi = [comment, row['nickname']]
# #     result.append(imsi)
                                  
# # result = pd.DataFrame(result, columns=sent_column)
# # outputname = './data/review_sent.csv'
# # result.to_csv(outputname, mode='w', encoding='utf-8', index=False)

# print('------------ finished --------')


# custom vocab list 만들기
sent_column = ['food']
result = []
for index, row in df3.iterrows():
    food = row['food']
    food = re.sub('[+,(\)]', '\n', str(food))
    result.append(food)
                                  
result = pd.DataFrame(result, columns=sent_column)
result.drop_duplicates('food', keep='first')
result.sort_values(by=['food'], axis=0, ascending=False)
outputname = './data/food.csv'
result.to_csv(outputname, mode='w', encoding='utf-8', index=False)

print('------------ finished --------')



# only_BMP_pattern = re.compile("["
#         u"\U00010000-\U0010FFFF" 
#                            "]+", flags=re.UNICODE)

# result=[]
# for index, row in df1.iterrows():
#     # comment = only_BMP_pattern.sub(r' ', str(row['review']))
#     pattern = '"'
#     comment = row['review']
#     comment = re.sub(pattern=pattern, repl=' ', string=str(comment))
#     imsi = [comment, row['point']]
#     result.append(imsi)

# result = pd.DataFrame(result, columns=sent_column)
# result.to_csv('./data/review_sen.csv', mode='w', encoding='utf-8', index=False)

# print('=======test2========')


# # 텍스트 파일로 만들기 -> setencepiece는 txt만 받음
# with open(input_file, 'a+', encoding='utf-8') as f:
#     for index, row in df2.iterrows():
#         f.write('"{}",{} \n'.format(row['review'], row['point']))
#         # if row['CATEGORY'] == '배달음식점':
#         #     f.write ('{}\n'.format(row['SENTENCE']))

# csv로 만들기
# food_voc = []

# with open('shopname.txt', 'r', encoding='utf-8') as f:
#     reader = csv.reader(f)
#     for row in f:
#         row = row.replace('\n', '')
#         food_voc.append(row)

# print(food_voc)