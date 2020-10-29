import re
import pandas as pd
from pandas import DataFrame

# 데이터 불러오기
df = pd.read_csv('./data/order_review(remove_userid_nan).csv', sep = ',', encoding= 'utf-8')
columns = ['or_id','order_time','review_cmnt','taste_rate','quantity_rate','delivery_rate','review_time','owner_cmnt','userid','shop_id','food_id']

# 이모티콘 제거
only_BMP_pattern = re.compile("["
        u"\U00010000-\U0010FFFF" 
                           "]+", flags=re.UNICODE)

result=[]
for index, row in df.iterrows():
    review_comment = row['review_cmnt']
    owner_comment = row['owner_cmnt']
    review_comment = only_BMP_pattern.sub(r' ', str(review_comment))
    owner_comment = only_BMP_pattern.sub(r' ', str(owner_comment))
    imsi = [row['or_id'],row['order_time'],review_comment,row['taste_rate'],row['quantity_rate'],row['delivery_rate'],row['review_time'],owner_comment,row['userid'],row['shop_id'],row['food_id']]
    result.append(imsi)

result = pd.DataFrame(result, columns=columns)
# 만약 이모티콘만 제거하고 싶으시면 여기서 주석 푸시고 저장할 파일 이름 지정해 주세요.
result.to_csv('review_filter.csv', mode='w', encoding='utf-8', index=False)
print('=======test1========')

# emoji_pattern = re.compile("["
#         u"\U0001F600-\U0001F64F"  # emoticons
#         u"\U0001F300-\U0001F5FF"  # symbols & pictographs
#         u"\U0001F680-\U0001F6FF"  # transport & map symbols
#         u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
#                            "]+", flags=re.UNICODE)
# result1=[]
# for index, row in result.iterrows():
    # customer = emoji_pattern.sub(r' ', row['review_cmnt'])
    # customer = re.sub('[❤️★♥️✨⭐♡♥☆⚽️⚾️❄❣️❤]', ' ', customer) 
    # pattern = '([ㄱ-ㅎㅏ-ㅣ]+)' #한글 자음 모음 제거 ㅋㅋㅋㅋ
    # customer = re.sub(pattern=pattern, repl='', string=customer)
    # customer = re.sub('[-=+,#/\:^$@*\"※~&%ㆍ!』\\‘;|\(\)\[\]\<\>`\'…》]', ' ', customer) #특수기호
    # customer = re.sub('  ', ' ', customer) #띄어쓰기가 2번이상 들어가면 -> 1번
#     owner_comment = emoji_pattern.sub(r' ', row['owner_cmnt'])
#     owner_comment = re.sub('[❤️★♥️✨⭐♡♥☆⚽️⚾️❄❣️❤]', ' ', owner_comment)
#     owner_comment = re.sub(pattern=pattern, repl='', string=owner_comment)
#     owner_comment = re.sub('[-=+,#/\:^$@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', ' ', owner_comment)
#     owner_comment = re.sub('  ', ' ', owner_comment)
#     imsi = [row['or_id'],row['order_time'],review_comment,row['taste_rate'],row['quantity_rate'],row['delivery_rate'],row['review_time'],owner_comment,row['userid'],row['shop_id'],row['food_id']]
#     result1.append(imsi)

# result1 = pd.DataFrame(result1, columns=sent_column)
# result1.to_csv('review_filter.csv', mode='w', encoding='utf-8', index=False)

# print('=======test2========')
