import pandas as pd
from pandas import DataFrame

shop = 'store.csv'

df = pd.read_csv(shop, sep = ',', encoding= 'utf-8' )


input_file = 'shopname1.txt'

# 텍스트 파일로 만들기 -> setencepiece는 txt만 받음
with open(input_file, 'a+', encoding='utf-8') as f:
    for index, row in df.iterrows():
        f.write('{} 1{}1\n'.format(row['name'], ('0'*(len(row['name'])-1))))
        # if row['CATEGORY'] == '배달음식점':
        #     f.write ('{}\n'.format(row['SENTENCE']))
