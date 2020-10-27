import pandas as pd
from pandas import DataFrame


# 일자(YYYYMMDD),연령,성별,발신지(시도),발신지(시군구),업종,평균기온,강수량

# print(df['연령'].value_counts())
# print(df['성별'].value_counts())
# print(df['업종'].value_counts())

# class Userfeatures():
#     def __init__(self):
#         # self.filepath = filepath
#         ...

#     def district_filter(self, filepath):
#         df = pd.read_csv(self.filepath, sep = ',', encoding= 'utf-8')

#         result = []
#         for index, row in df.iterrows():
#             if df['발신지(시군구)'] == (['강남구'] or ['서초구']) :
#                 result.append(row)

#         print(result)
#         print('=========finished=============')


# if __name__ == '__main__':
#     # filepath = 'order.csv'
#     Userfeatures().district_filter('order.csv')

filepath = 'order.csv'
df = pd.read_csv(filepath, sep = ',', encoding= 'utf-8')
column = ['일자(YYYYMMDD)','연령','성별','발신지(시도)','발신지(시군구)','업종','평균기온','강수량']
print(dict(df['업종'].value_counts()))
print(dict(df['연령'].value_counts()))
#{40: 35578, 30: 21183, 50: 19971, 60: 4230, 20: 2659, 70: 2}  #20&30 40&50 60&70 -> propertion으로 결정

# gender
female = []
male= []
for index, row in df.iterrows():
    if row['발신지(시군구)'] == '강남구' :
        if row['성별'] == '여성' :
            female.append(row)
        elif row['성별'] == '남성':
            male.append(row)

female =pd.DataFrame(female,columns=column)
male =pd.DataFrame(male,columns=column)

female_category = dict(female['업종'].value_counts())
male_category = dict(male['업종'].value_counts())

female_category = dict(female['연령'].value_counts())
male_category = dict(male['연령'].value_counts())

print(female_category)
print(male_category)

print('=========finished=============')


# print(df['연령'].value_counts())
# print(df['성별'].value_counts())
# print(df['업종'].value_counts())

 

# 서울시
# {'한식': 55566, '치킨': 14413, '중식': 10468, '양식': 1890, '카페': 613, '분식': 612, '간식': 41, '일식': 20}
# ['한식', '치킨', '중식', '피자양식',  '카페디저트' , '일식돈까스', '분식', '1인분주문', '족발보쌈', '편의점','야식']

# 서초구
# 여성 = {'한식': 1123, '치킨': 150, '중식': 98, '양식': 70, '분식': 11, '간식': 3, '카페': 1}
# 남성 = {'한식': 1269, '중식': 64, '양식': 11, '치킨': 4}

# 강남구
# 여성 = {'한식': 1072, '치킨': 85, '중식': 78, '양식': 55, '분식': 3, '카페': 3, '간식': 2}
# 남성 = {'한식': 1117, '중식': 88, '양식': 17, '일식': 1}

# comment = './csv/comment.csv'
# df1 = pd.read_csv(comment, sep = ',', encoding= 'utf-8')
# column_gender=['orderid','comment']

# split_df = df1['owner_comment'].str.split(' ', expand=True) # 파이썬 문자열 spilt

# age = pd.concat([df1, split_df], axis=1)
# print(age.head(10))
# print('=========finished=============')





# string 
# ['야식', '테이크아웃', '피자양식', '한식', '치킨', '분식', '중식', '1인분주문', '일식돈까스', '족발보쌈', '프랜차이즈', '카페디저트', '방문식사', '편의점', '예약픽업', '강남맛집배달', '', 'D마트']
# category = 'category.csv'
# mycategory = pd.read_csv(category, sep = ',', encoding= 'utf-8')

# split_category = mycategory['category'].str.strip('][') # 파이썬 문자열 spilt
# split_category = split_category.str.split(',', expand=True)
 
# category = pd.concat([mycategory, split_category], axis=1)

# category = category.drop(['category'], axis=1)

# print(category.head(20))

# for idx in range(len(category)):
#     for i in range(2, 16):
#         if category.iloc[idx, i] == '테이크아웃' or '방문식사' or '예약픽업' or '강남맛집배달' or 'D마트' or '': 
#             category.iloc[idx, 2] = None

# category = category.dropna(how='all')

# # category['category'] = category[[0,1]].apply(','.join, axis=1)
# category['category'] = category[0].str.cat(category[1], sep=',')

# category.to_csv('category_filter1.csv', mode='w', encoding='utf-8', index=False)


twenties=[]
thirties=[]
fourties=[]
fifties=[]
seninor = []
maletotal=[]

for index, row in df.iterrows():
    if row['발신지(시군구)'] == '강남구' :
        if row['연령'] == 20 and row['성별'] == '남성':
            twenties.append(row)
        elif row['연령'] == 30 and row['성별'] == '남성':
            thirties.append(row)
        elif row['연령'] == 40 and row['성별'] == '남성':
            fourties.append(row)
        elif row['연령'] == 50 and row['성별'] == '남성':
            fifties.append(row)
        elif (row['연령'] == 60 or row['연령'] == 70) and row['성별'] == '남성':
            seninor.append(row)
        else:
            maletotal.append(row)
            

twenties=pd.DataFrame(thirties,columns=column)
thirties=pd.DataFrame(thirties,columns=column)
fourties=pd.DataFrame(fourties,columns=column)
fifties=pd.DataFrame(fifties,columns=column)
seninor =pd.DataFrame(seninor,columns=column)


# twentiesfemale=[]
# twentiesmale=[]

# for index, row in twenties.iterrows():
#     if row['성별'] == '여성' :
#         twentiesfemale.append(row)
#     else :
#         twentiesmale.append(row)
            
# twentiesmale=pd.DataFrame(twentiesmale,columns=column)
# twentiesfemale=pd.DataFrame(twentiesfemale,columns=column)

# twentiesfemale = dict(twentiesfemale['업종'].value_counts())
# # twentiesmale = dict(twentiesmale['업종'].value_counts())

# print(twentiesfemale)
# print(twentiesmale)
# print('====check====')
# print(twenties.head(20))

twenties=dict(twenties['업종'].value_counts()) # {'한식': 40, '양식': 5}
thirties=dict(thirties['업종'].value_counts()) # {'한식': 706, '양식': 45, '중식': 28, '카페': 3, '간식': 1, '일식': 1}
fourties=dict(fourties['업종'].value_counts()) # {'한식': 724, '중식': 138, '치킨': 85, '양식': 22, '분식': 3, '간식': 1}
fifties=dict(fifties['업종'].value_counts()) # {'한식': 658}
seninor = dict(seninor['업종'].value_counts()) # {'한식': 61}

# ===female===                                                                                        =====male====
# {'한식': 346, '양식': 31, '카페': 3, '중식': 1, '간식': 1}                               {'한식': 360, '중식': 27, '양식': 14, '일식': 1}
# {'한식': 346, '양식': 31, '카페': 3, '중식': 1, '간식': 1}                                {'한식': 360, '중식': 27, '양식': 14, '일식': 1}
# {'한식': 362, '치킨': 85, '중식': 77, '양식': 21, '분식': 3, '간식': 1}                   {'한식': 362, '중식': 61, '양식': 1}
# {'한식': 324}                                                                             {'한식': 334}
# {'한식': 2}                                                                               {'한식': 59}

# twenties_category=dict(twenties['성별'].value_counts()) #{'여성': 41, '남성': 4}
# thirties_category=dict(thirties['성별'].value_counts()) #{'남성': 402, '여성': 382}
# fourties_category=dict(fourties['성별'].value_counts()) #{'여성': 549, '남성': 424}
# fifties_category=dict(fifties['성별'].value_counts()) #{'남성': 334, '여성': 324}
# seninor_category = dict(seninor['성별'].value_counts()) #{'남성': 59, '여성': 2}


print('================category==========')
print(twenties)
print(thirties)
print(fourties)
print(fifties)
print(seninor)

# print('===================gender==========')
# print(twenties_category) 
# print(thirties_category)
# print(fourties_category)
# print(fifties_category)
# print(seninor_category)


# print('=========finished=============')




# noise = ['테이크아웃' ,'방문식사', '예약픽업', '강남맛집배달', 'D마트', '' ]
# category_food = pd.concat([mycategory, split_category], axis=1)
# print(category_food.head(20))

# mycategory['category'] = mycategory['category'].astype(str)    .to_list // .to_string

# result = []
# for row, index in mycategory.iterrows():
#     item = row['category'] 
#     item = item.replace('[', '')
#     item = item.replace(']', '')
#     result.append(row)
    
# result = pd.Datafram(result,column=category_index)
# print(result)

# category_index = ['shopid', 'category']
# categories = mycategory.to_dict(orient='records')
# print(categories)
# print(type(categories))

# # result = []
# # for value in categories:
#     itemmycategory['category']

#     break
#     value = value.replace('[', '')
#     value = value.replace(']', '')
#     item = value.split(',')
    

#     result.append(item)

# print(result)

# result = []
# for row, index in mycategory.iterrows():
#     item = row['category'] 
#     item = item.replace('[', '')
#     item = item.replace(']', '')
#     result.append(row)
    
# result = pd.Datafram(result,column=category_index)
# print(result)



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

# noise = ['테이크아웃' ,'방문식사', '예약픽업', '강남맛집배달', 'D마트', '' ]

# for index, row in mycategory.iterrows():
#     idx = mycategory['category'].split(',')
#     if idx not in pure_category:
#         data.append(mycategory['storeid'])

# print(data)
