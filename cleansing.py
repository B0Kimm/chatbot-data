import re
import pandas as pd
from pandas import DataFrame


# # text = '희안하게 로뎀휴일인 월욜마다 피자가 땡겨서어쩔수없이 한동안 다른곳들 이용해봤는데...로뎀만한곳이 없어서어제부터 참고참다가 오늘 주문했네요😁😁😁쩝~맛나게 먹어볼까요~~??🎶🎶윙도 자~~알 먹겠습니당!! ~^.^~,항상감사합니다 풍성한토핑 맛난피자로 보답할께요'
# text = '먹은사진이 없어서 부득이하게 이렇게 올려요 사장님 새우먹고싶을때마다 올게요 이런집은 혼내줘야되요ㅠㅠㅠ 저 소짜리 시켰는데 왜 3일♡이나 먹게하시는거예요??ㅠㅠㅠㅠㅠ 맛에서 하나뺀거는 제가 매운거 못먹는편은 아닌데 살짝 매큼했어요ㅜ 보완할겸 제 요구채울겸 사장님 주머니채울겸 채소추가 메뉴에 넣어주십셔 잘먹었습니당ㅎㅎㅎㅎ'
# textb = '닭반마리이상에 국물이 진짜 매큼달큰하니 너무 맛잇어서 밥비벼먹고싶엇어요ㅠㅜㅜㅜ 사진은 다먹은짤.. 근데 채소나 감자나 국물이 별로없어서 조금 아쉬웟습니다ㅜ 추가할 수 있는 란 만들어두면 좋을것같아요 *밥 안옵니다 오는줄알앗지만 저처럼 생각하시는 분들도잇을테니 참고하세요!'

# test = '배달도빠르고 서비스도 맛있고 다 좋았어요 👍🏻'
# test2 = '👍👍👍👍😅👍👍'
# test3 = '총알 배달  맛도 최고💋'
# test4 = '😋😋🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳'


df = pd.read_csv('test4.csv', sep = ',', encoding= 'utf-8')


only_BMP_pattern = re.compile("["
        u"\U00010000-\U0010FFFF" 
                           "]+", flags=re.UNICODE)
# print(only_BMP_pattern.sub(r'', test))
# print(only_BMP_pattern.sub(r'', test2))
# print(only_BMP_pattern.sub(r'', test3))
# print(only_BMP_pattern.sub(r'', test4))


# split_category = mycategory['category'].str.strip('][') # 파이썬 문자열 spilt

# print(type(df['customer_comment']))
review_column = ['shopid','menu_summary','nickname','rating','customer_comment','owner_comment']

only_BMP_pattern = re.compile("["
        u"\U00010000-\U0010FFFF" 
                           "]+", flags=re.UNICODE)

result=[]
for index, row in df.iterrows():
    customer = only_BMP_pattern.sub(r' ', str(row['customer_comment']))
    answer = only_BMP_pattern.sub(r' ', str(row['owner_comment']))
    imsi = [row['shopid'],row['menu_summary'],row['nickname'],row['rating'], customer, answer]
    result.append(imsi)

result = pd.DataFrame(result, columns=review_column)
# result.to_csv('test.csv', mode='w', encoding='utf-8', index=False)


# df.to_csv('test.csv', mode='w', encoding='utf-8', index=False)

print('=======test1========')

# df['customer_comment'] = only_BMP_pattern.sub(r'', df['customer_comment'].apply(lambda _: str(_)))
# df['owner_comment'] = only_BMP_pattern.sub(r'', df['customer_comment'].astype(str))



emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags=re.UNICODE)
result1=[]
for index, row in result.iterrows():
    customer = emoji_pattern.sub(r' ', row['customer_comment'])
    customer = re.sub('[❤️★♥️✨⭐♡♥☆⚽️⚾️❄❣️❤]', ' ', customer) 
    pattern = '([ㄱ-ㅎㅏ-ㅣ]+)' #한글 자음 모음 제거 ㅋㅋㅋㅋ
    customer = re.sub(pattern=pattern, repl='', string=customer)
    customer = re.sub('[-=+,#/\:^$@*\"※~&%ㆍ!』\\‘;|\(\)\[\]\<\>`\'…》]', ' ', customer) #특수기호
    customer = re.sub('  ', ' ', customer) #띄어쓰기가 2번이상 들어가면 -> 1번
    answer = emoji_pattern.sub(r' ', row['owner_comment'])
    answer = re.sub('[❤️★♥️✨⭐♡♥☆⚽️⚾️❄❣️❤]', ' ', answer)
    answer = re.sub(pattern=pattern, repl='', string=answer)
    answer = re.sub('[-=+,#/\:^$@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', ' ', answer)
    answer = re.sub('  ', ' ', answer)
    imsi = [row['shopid'],row['menu_summary'],row['nickname'],row['rating'], customer, answer]

    result1.append(imsi)

result1 = pd.DataFrame(result1, columns=review_column)
result1.to_csv('test4.csv', mode='w', encoding='utf-8', index=False)

print('=======test2========')

# def cleansing(text):
#     pattern = '([ㄱ-ㅎ ㅏ-1]+)' #한글 자음 모음 제거
#     text = re.sub(pattern=pattern, repl='', string=text)
# text = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', '', text)
# print(text)

# #character ngram
# n = 2
# result = []
# for a in range(len(text)-n + 1):
#     result.append(text[a:a+n])
# print(result)

# resultb = []
# for b in range(len(textb)-n + 1):
#     resultb.append(textb[b:b+n])
# print(resultb)


# cnt = 0
# r = []
# for i in result:
#     for j in resultb:
#         if i == j:
#             cnt += 1
#             r.append(i)
# print(cnt/len(result))

