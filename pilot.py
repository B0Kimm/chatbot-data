import json
import csv
import pandas as pd



review = './csv/review.csv'
food = './csv/menu.csv'
store = './csv/store.csv'
category ='category.csv'

myreview = pd.read_csv(review, sep = ',', encoding= 'utf-8')
myfood = pd.read_csv(food, sep = ',', encoding= 'utf-8')
mystore = pd.read_csv(store, sep = ',', encoding= 'utf-8')
mycategory = pd.read_csv(category, sep = ',', encoding= 'utf-8')


Review 
# result=[]
# review_columns = ['id', 'nickname','orderid','menu_summary', 'comment']
# for index, row in myreview.iterrows():
#     imsi = [row['storeid'], row['nickname'], row['customerid'],row['menu_summary'], row['comment']]
#     result.append(imsi)

# result = pd.DataFrame(result, columns= review_columns)





# print(myframe.head(10))

# print(myframe['nickname'].value_counts())
# nickname = myframe['nickname'].unique()



# Review 
# result=[]
# review_columns = ['id', 'nickname','orderid','menu_summary', 'comment']
# for index, row in myreview.iterrows():
#     imsi = [row['storeid'], row['nickname'], row['customerid'],row['menu_summary'], row['comment']]
#     result.append(imsi)

# result = pd.DataFrame(result, columns= review_columns)

# # 스토어 아이디/ 주소
# outcome = []
# store_columns = [row['nickname'] == 'do**']
# for idx, row in mystore.iterrows():
#     temp = [int(row['id']), row['name'], row['address'], row['distance'], row['lat'], row['lng'],row['delivery_fee'], row['min_order_amount'], row['open_time_description'], row['review_avg'],row['categories'] ]
#     outcome.append(temp)

# outcome = pd.DataFrame(outcome, columns= store_columns)

# print(outcome.head(20))

# # left는 df1을 기준으로 right는 df2를 기준으로 합치기(값이 없을 경우 Na)

# data = pd.merge(outcome, myreview, on='storeid', how='right')

# print(data.head(20))

# columns = ['id','name','lat','lng','동','지번','nickname','orderid','menu_summary','comment']

# # print(myframe['구'].value_counts(ascending=True))

# result = []
# for index, row in data.iterrows():
#     if row['nickname'] == 'do**' :
#         imsi = [int(row['storeid']), row['name'], row['address'], row['distance'], row['lat'], row['lng'],row['delivery_fee'], row['min_order_amount'], row['open_time_description'], row['review_avg'],row['categories'],\
#                 row['comment'],row['rating'],row['menu_summary'],row['rating_quantity'],row['rating_taste'],row['rating_delivery'],row['time'],row['nickname'],row['customerid'] ]
#         result.append(imsi)
       

# result = pd.DataFrame(result, columns=columns)

# # outcome.to_csv('yeongdeungpo_do.csv', mode='w', encoding='utf-8', index=False)

# result.to_csv('yeongdeungpo_do_1.csv', mode='w', encoding='utf-8', index=False)

# filename2='total.csv'
# result.to_csv(filename2, mode='w', encoding='utf-8', index=False)



# filename = 'test.csv'

# data1 = pd.read_csv(filename, sep = ',', encoding= 'utf-8')

# data1 = data1['nickname'].sort_values(ascending=True)
# print(data1.head(50))

# csvfilename = 'store.csv'
# myframe.to_csv(csvfilename, mode= 'w', encoding='utf-8',index=False)
# print(f'--------{csvfilename} done -------------')

# flatten 중첩리스트
# categories = mycategory['category'].tolist()

# # flatten 중첩리스트
# # for item in categories:
# #     print(type(item))
# #     for word in item:
# #         print(type(word))

# string 
# ['야식', '테이크아웃', '피자양식', '한식', '치킨', '분식', '중식', '1인분주문', '일식돈까스', '족발보쌈', '프랜차이즈', '카페디저트', '방문식사', '편의점', '예약픽업', '강남맛집배달', '', 'D마트']
# categories = mycategory['category'].tolist()

# result = []
# for item in categories:
#     item = item.replace('[', '')
#     item = item.replace(']', '')
#     item = item.replace(',', '')
#     item = item.replace("'", "")
#     words = item.split(' ')
#     for word in words:
#         if word not in result:
#             result.append(word)

# print(result)

# noise = [ '테이크아웃' ,'방문식사', '예약픽업', '강남맛집배달', 'D마트', '' ]

# for index, row in mycategory.iterrows():
#     idx = mycategory['category'].split(',')
#     if idx not in pure_category:
#         data.append(mycategory['storeid'])

# print(data)


twenties=[]
thirties=[]
fourties=[]
fifties=[]
seninor = []

for index, row in df.iterrows():
    if row['발신지(시군구)'] == '강남구' :
        if row['연령'] == '20' :
            twenties.append(row)
        elif row['연령'] == '30':
            thirties.append(row)
        elif row['연령'] == '40':
            fourties.append(row)
        elif row['연령'] == '50':
            fifties.append(row)
        else:
            seninor.append(row)
            
twenties=pd.DataFrame(twenties,columns=column)
thirties=pd.DataFrame(thirtie,columns=column)
fourties=pd.DataFrame(fourties,columns=column)
fifties=pd.DataFrame(fifties,columns=column)
seninor =pd.DataFrame(seninor,columns=column)

twenties=dict(female['업종'].value_counts())
thirties=dict(female['업종'].value_counts())
fourties=dict(female['업종'].value_counts())
fifties=dict(female['업종'].value_counts())
seninor = dict(female['업종'].value_counts())

twenties_category=dict(female['성별'].value_counts())
thirties_category=dict(female['성별'].value_counts())
fourties_category=dict(female['성별'].value_counts())
fifties_category=dict(female['성별'].value_counts())
seninor_category = dict(female['성별'].value_counts())

for index, row in twenties.iterrows():
    if row['발신지(시군구)'] == '강남구' :
        if row['연령'] == '20' :
            twenties.append(row)
        elif row['연령'] == '30':
            thirties.append(row)
        elif row['연령'] == '40':
            fourties.append(row)
        elif row['연령'] == '50':
            fifties.append(row)
        else:
            seninor.append(row)


print('================category==========')
print(twenties)
print(thirties)
print(fourties)
print(fifties)
print(seninor)

print('===================gender==========')
print(twenties_category)
print(thirties_category)
print(fourties_category)
print(fifties_category)
print(seninor_category)


print('=========finished=============')
