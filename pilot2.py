import pandas as pd
import pandas as pd
import json
import csv
filename = './csv/review.csv'
# # filename = 'yeongdeungpo.csv'

myframe = pd.read_csv(filename, sep = ',', encoding= 'utf-8')

print(myframe.columns)
# columns = ['id','name','lat','lng','address', '동','지번','nickname','orderid','menu_summary','comment']

# # # print(myframe['구'].value_counts(ascending=True))

# row에서 필요한 셀만 추가
# result = []
# for index, row in myframe.iterrows():
#     if row['구'] == '강남구' :
#         result.append(row)
        # comment = row['comment']
        # comment = comment.replace('\r', ' ')
#       comment = comment.replace('\n', ' ')
#         imsi = [row['id'], row['name'], row['lat'],row['lng'], row['address'], row['동'], row['지번'], row['nickname'],row['orderid'],row['menu_summary'],comment ]
#         result.append(imsi)

# result = pd.DataFrame(result, columns=columns)
# result.to_csv('gangnam.csv', mode='w', encoding='utf-8', index=False)


# outcome = []
# for index, row in result.iterrows():
#     if row['nickname'] == 'do**' :
#         imsi = [row['id'], row['name'], row['lat'],row['lng'], row['동'], row['지번'], row['nickname'],row['orderid'],row['menu_summary'],row['comment'] ]
#         outcome.append(imsi)

# outcome = pd.DataFrame(outcome, columns=columns)

# # 두개의 데이터 프레임을 옆으로 붙이기
# data = pd.concat([myframe, result],axis=1)
# print(data.head(20))

# # index 'id'로 데이터 합치기
# mergedata = pd.merge(data, outcome, on='id', how='left')
# print(mergedata.head())

# # outcome.to_csv('yeongdeungpo_do.csv', mode='w', encoding='utf-8', index=False)

# outcome.to_csv('yeongdeungpo_do_.csv', mode='w', encoding='utf-8', index=False)



# print(result.head(10))

# data = pd.concat([myframe, result],axis=1)
# print(data.head(20))

# outcome=[]
# review_columns = ['id', 'nickname','orderid','menu_summary', 'comment']
# for index, row in myreview.iterrows():
#     imsi = [row['storeid'], row['nickname'], row['customerid'],row['menu_summary'], row['comment']]
#     outcome.append(imsi)

# outcome = pd.DataFrame(outcome, columns= review_columns)
# # merge는 같은 indext, join은 merge와 비슷
# # data = pd.merge(myframe, result, on='id', how='left')
# # data = myframe.join(result)

# mergedata = pd.merge(data, outcome, on='id', how='left')

# print(mergedata.head())
# filename2='test3.csv'
# mergedata.to_csv(filename2, mode='w', encoding='utf-8', index=False)


# # outputname = 'new_data.csv'
# # data.to_csv(outputname, mode='w', encoding='utf-8', index=False)


# # bi-gram and tri-gram model by nltk
# import nltk

# text = ...

# text = text.split()
# result = nltk.bigrams(text)

# # n gram without nltk
# def n_gram(text, n):
#     result = []
#     words = text.split()
#     for i in range(len(words) - (n-1)):
#         result.append(' '.join(words[i:i+n]))
#     result result

# n=2
# print(n_gram(text,n))


# input_file = r'C:\Users\USER\data\json\review(seoul)'
# testcolums = [ 'shopid', 'menu_summary', 'nickname', 'rating', 'customercomment',  'ownercomment' ]

# class YogiyoModel :
#     def __init__(self, filename):
#         self.filename = filename
#         self.writer = None

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
    # allFile_list = glob.glob(os.path.join(input_file, 'yogiyo_*' +'.csv'))
    
    # for file in allFile_list :
    #         for file in allFile_list :
    #             YogiyoModel(f'{file}').merge()
    # filename = '.\csv\seoul.csv'
    # YogiyoModel('./json/review(seoul)/yogiyo_review(0~1000).json').chatbot_csv()