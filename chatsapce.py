from chatspace import ChatSpace
import torch

# chatspace
spacer = ChatSpace()


shop_voc = []

with open('shopname.txt', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in f:
        row = row.replace('\n', '')
        shop_voc.append(row)

food = './data/food.csv'

df3 = pd.read_csv(food, sep = ',', encoding= 'utf-8')

food_voc = []
for index, row in df3.iterrows():
    food = row['food']
    food_voc.append(food)
                                  
voca = shop_voc.extend(food_voc)

df = pd.read_csv('review_sen.csv', sep = ',', encoding= 'utf-8')

sent_column = ['review', 'point']
contents = []
for index, row in df.iterrows():
    review = spacer.space(row['review'], custom_voca = voca)
    contents.append([review, row['point']])

contents = pd.DataFrame(contents, columns=sent_column)
contents.to_csv('test.csv', mode='w', encoding='utf-8', index=False)


# text1 = '감사합니다 앞으로도 잘부탁드려요 풍성한토핑 맛난피자로 보답하겠습니다'
# text2 = '맛있게 잘 먹었습니다~'
# text3 = '마시써효!!!떡볶이도좋아요'
# text4 = '불고기는 처음 시켜봤는데 상상 그이상....'
# text5 = '냠냠~너무 맛있어용^^ 또 시켜먹어요넘나맛있네여피짜로덤왜인기가잇는지알겟둠원픽예약임툐쿄'
# text6 = '영등포피자중 이찌방'
# text7 = 'ㅋㅋㅋㅋ 파인애플 당연 추가한줄알고 실수했네요죄송염~~오늘도 맛나게 잘 먹겠습니다^^샐러드가 생각보다 푸짐하게 왔네요'


# print('======chatspace====')
# spacer.space(text3, batch_size=64)
# spacer.space(text5, batch_size=64)
# spacer.space(text6, batch_size=64)
# spacer.space(text7, batch_size=64)