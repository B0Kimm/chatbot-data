import pandas as pd
from pandas import DataFrame
import numpy as np

# filename = 'user_df.csv'

# df = pd.read_csv(filename, sep = ',', encoding= 'utf-8')

# new_myframe = pd.DataFrame(df.addr.str.split(' ').tolist())

# print(new_myframe.head(20))
# columns = ['구']


# result = []
# for index, row in new_myframe.iterrows():
#     imsi = [row[1]]
#     result.append(imsi)

# result = pd.DataFrame(result, columns=columns)
# data = pd.concat([df, result],axis=1)

# print(data['구'].value_counts())

# gangnam = []
# seocho = []
# for index, row in data.iterrows():
#     if row['구'] == '강남구':
#         gangnam.append(row)
#         # female_g = df.groupby('여성').apply(samlping_func, smaple_pct=0.51)
#         # female = data.sample(n=889, random_state=1)
#         # female['gender'] = '여성'
#     else:
#         seocho.append(row)
#         # female_s = df.groupby('여성').apply(samlping_func, smaple_pct=0.52)
#         # sfemale = data.sample(n=329, random_state=1) 
#         # sfemale['gender'] = '여성'

# columns = ['userid','pwd','name','age','gender','addr','lat','lng', '구']

# gangnam = pd.DataFrame(gangnam, columns=columns)
# seocho = pd.DataFrame(seocho, columns=columns)

# sample_gang = gangnam.sample(n=889, random_state=1)
# sample_gang['gender'] = '여성'
# gang4 = sample_gang.sample(n=42, random_state=1)
# gang4['age'] = '40'

# print(sample_gang.head(10))

# sample_seo = seocho.sample(n=329, random_state=1)
# sample_seo['gender'] = '여성'
# seo4 = sample_seo.sample(n=46, random_state=1)
# seo4['age'] = '40'

# fourty = pd.concat([gang4,seo4 ])



# columns = ['userid','pwd','name','age','gender','addr','lat','lng', '구']

# test = pd.merge(data, fourty, how='left', on='userid')

# outcome=[]
# for index, row in test.iterrows():
#     if row['gender_y'] != None:
#         imsi = [row['userid'],row['pwd_x'],row['name_x'],row['age_y'],row['gender_x'],row['addr_x'],row['lat_x'],row['lng_x'], row['구_x'] ]
#         outcome.append(imsi)
#         # female_g = df.groupby('여성').apply(samlping_func, smaple_pct=0.51)
#         # female = data.sample(n=889, random_state=1)
#         # female['gender'] = '여성'

#         # female_s = df.groupby('여성').apply(samlping_func, smaple_pct=0.52)
#         # sfemale = data.sample(n=329, random_state=1) 
#         # sfemale['gender'] = '여성'

# outcome = pd.DataFrame(outcome, columns=columns)
# outcome.to_csv('40.csv', mode='w', encoding='utf-8', index=False) 
'''============================40================'''
filename = '40.csv'

df = pd.read_csv(filename, sep = ',', encoding= 'utf-8')

nofourtygang = []
nofourtyseo =[]

columns = ['userid','pwd','name','age','gender','addr','lat','lng', '구']

for index, row in df.iterrows():
    if row['age'] != '40.0' and row['구'] == '강남구':
        nofourtygang.append(row)
        # female_g = df.groupby('여성').apply(samlping_func, smaple_pct=0.51)
        # female = data.sample(n=889, random_state=1)
        # female['gender'] = '여성'
    elif row['구'] == '서초구' and row['age'] == None:
        nofourtyseo.append(row)
        # female_s = df.groupby('여성').apply(samlping_func, smaple_pct=0.52)
        # sfemale = data.sample(n=329, random_state=1) 
        # sfemale['gender'] = '여성'

nofourtygang = pd.DataFrame(nofourtygang, columns=columns)
print(nofourtygang.head(20))
nofourtyseo = pd.DataFrame(nofourtyseo, columns=columns)

# gang3 = nofourtygang.sample(n=29, random_state=1)
# gang3['age'] = '30'

# seo3 = nofourtyseo.sample(n=25, random_state=1)
# seo3['age'] = '30'

# thirty = pd.concat([gang3,seo3 ])



# columns = ['userid','pwd','name','age','gender','addr','lat','lng', '구']

# test = pd.merge(data, thirty, how='left', on='userid')

# outcome2=[]
# for index, row in test.iterrows():
#     if row['gender_y'] != None:
#         imsi = [row['userid'],row['pwd_x'],row['name_x'],row['age_y'],row['gender_x'],row['addr_x'],row['lat_x'],row['lng_x'], row['구_x'] ]
#         outcome2.append(imsi)
#         # female_g = df.groupby('여성').apply(samlping_func, smaple_pct=0.51)
#         # female = data.sample(n=889, random_state=1)
#         # female['gender'] = '여성'

#         # female_s = df.groupby('여성').apply(samlping_func, smaple_pct=0.52)
#         # sfemale = data.sample(n=329, random_state=1) 
#         # sfemale['gender'] = '여성'

# outcome2 = pd.DataFrame(outcome2, columns=columns)
# outcome2.to_csv('30.csv', mode='w', encoding='utf-8', index=False) 
# '''============================30================'''

# nofourthirtygang = []
# nofourthirtyseo =[]

# for index, row in outcome2.iterrows():
    
#     if row['구'] == '강남구' and row['gender'] == '여성' and row['age'] == None:
#         nofourtygang.append(row)
#         # female_g = df.groupby('여성').apply(samlping_func, smaple_pct=0.51)
#         # female = data.sample(n=889, random_state=1)
#         # female['gender'] = '여성'
#     elif row['구'] == '서초구' and row['gender'] == '여성' and row['age'] == None:
#         nofourtyseo.append(row)
#         # female_s = df.groupby('여성').apply(samlping_func, smaple_pct=0.52)
#         # sfemale = data.sample(n=329, random_state=1) 
#         # sfemale['gender'] = '여성'
# nofourthirtygang = pd.DataFrame(nofourtygang, columns=columns)
# nofourthirtyseo = pd.DataFrame(nofourtyseo, columns=columns)

# gang2 = nofourthirtygang.sample(n=3, random_state=1)
# gang2['age'] = '20'
# seo2 = nofourthirtyseo.sample(n=2, random_state=1)
# seo2['age'] = '20'

# tweenty = pd.concat([gang2,seo2 ])

# columns = ['userid','pwd','name','age','gender','addr','lat','lng', '구']

# test = pd.merge(data, tweenty, how='left', on='userid')

# outcome2=[]
# for index, row in test.iterrows():
#     if row['gender_y'] != None:
#         imsi = [row['userid'],row['pwd_x'],row['name_x'],row['age_y'],row['gender_x'],row['addr_x'],row['lat_x'],row['lng_x'], row['구_x'] ]
#         outcome2.append(imsi)
#         # female_g = df.groupby('여성').apply(samlping_func, smaple_pct=0.51)
#         # female = data.sample(n=889, random_state=1)
#         # female['gender'] = '여성'

#         # female_s = df.groupby('여성').apply(samlping_func, smaple_pct=0.52)
#         # sfemale = data.sample(n=329, random_state=1) 
#         # sfemale['gender'] = '여성'

# outcome3 = pd.DataFrame(outcome3, columns=columns)


# '''=====================================20====================='''

# nofiftygang = []
# nofiftyseo =[]

# for index, row in outcome3.iterrows():
    
#     if row['구'] == '강남구' and row['gender'] == '여성' and row['age'] == None:
#         nofourtygang.append(row)
#         # female_g = df.groupby('여성').apply(samlping_func, smaple_pct=0.51)
#         # female = data.sample(n=889, random_state=1)
#         # female['gender'] = '여성'
#     elif row['구'] == '서초구' and row['gender'] == '여성' and row['age'] == None:
#         nofourtyseo.append(row)
#         # female_s = df.groupby('여성').apply(samlping_func, smaple_pct=0.52)
#         # sfemale = data.sample(n=329, random_state=1) 
#         # sfemale['gender'] = '여성'
# nofiftygang = pd.DataFrame(nofourtygang, columns=columns)
# nofiftyseo = pd.DataFrame(nofourtyseo, columns=columns)

# gang5 = nofiftygang.sample(n=25, random_state=1)
# gang4['age'] = '50'
# seo5 = nofiftyseo.sample(n=24, random_state=1)
# seo5['age'] = '50'

# fifty = pd.concat([gang2,seo2 ])

# columns = ['userid','pwd','name','age','gender','addr','lat','lng', '구']

# test = pd.merge(data, fifty, how='left', on='userid')

# outcome2=[]
# for index, row in test.iterrows():
#     if row['gender_y'] != None:
#         imsi = [row['userid'],row['pwd_x'],row['name_x'],row['age_y'],row['gender_x'],row['addr_x'],row['lat_x'],row['lng_x'], row['구_x'] ]
#         outcome2.append(imsi)
#         # female_g = df.groupby('여성').apply(samlping_func, smaple_pct=0.51)
#         # female = data.sample(n=889, random_state=1)
#         # female['gender'] = '여성'

#         # female_s = df.groupby('여성').apply(samlping_func, smaple_pct=0.52)
#         # sfemale = data.sample(n=329, random_state=1) 
#         # sfemale['gender'] = '여성'

# outcome4 = pd.DataFrame(outcome4, columns=columns)
# outcome4['age'] = outcome4['age'].fillna('60')


# # age1 = pd.concat([gang2,gang3])
# # age2 = pd.concat([gang4,gang5])
# # sample1 = pd.concat([age1,age2])

# # print(sample_gang.head(10))

# # sample_seo = seocho.sample(n=329, random_state=1)
# # sample_seo['gender'] = '여성'
# # # seo2 = sample_seo.sample(n=2, random_state=1)
# # # seo2['age'] = '20'
# # # seo3 = seo2.sample(n=25, random_state=1)
# # # gaseo3['age'] = '30'
# # # seo4 = seo3.sample(n=46, random_state=1)
# # # seo4['age'] = '40'
# # # seo5 = seo4.sample(n=24, random_state=1)
# # # seo5['age'] = '50'

# # # age3 = pd.concat([seo2,seo3])
# # # age4 = pd.concat([seo4,seo5])
# # # sample2 = pd.concat([age3,age4])

# # print(sample_seo.head(10))
# # female = pd.concat([sample_seo,sample_gang ])
# # test = pd.merge(data, female, how='left', on='userid')

# # outcome=[]
# # for index, row in test.iterrows():
# #     if row['gender_y'] != None:
# #         imsi = [row['userid'],row['pwd_x'],row['name_x'],row['age_x'],row['gender_y'],row['addr_x'],row['lat_x'],row['lng_x'], row['구_x'] ]
# #         outcome.append(imsi)
# #         # female_g = df.groupby('여성').apply(samlping_func, smaple_pct=0.51)
# #         # female = data.sample(n=889, random_state=1)
# #         # female['gender'] = '여성'

# #         # female_s = df.groupby('여성').apply(samlping_func, smaple_pct=0.52)
# #         # sfemale = data.sample(n=329, random_state=1) 
# #         # sfemale['gender'] = '여성'

# # outcome = pd.DataFrame(outcome, columns=columns)
# # outcome['gender'] = outcome['gender'].fillna('남성')

# # outcome.to_csv('gender.csv', mode='w', encoding='utf-8', index=False)   


  