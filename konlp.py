from eunjeon import Mecab
import sentencepiece as spm
from pandas import DataFrame
import pandas as pd

# review = './csv/chatbot.csv'

# df = pd.read_csv(review, sep = ',', encoding= 'utf-8' )
# df1 = pd.read_excel('A 음식점(15,726).xlsx', sheet_name='15,726')
# df2 = pd.read_excel('D 소매점(14,949).xlsx', sheet_name='Sheet1')
# df3 = pd.read_excel('F 카페(7,859).xlsx', sheet_name='Sheet1')
# df4 = pd.read_excel('B 의류(15,826).xlsx', sheet_name='Sheet1')
# df5 = pd.read_excel('C 학원(4,773).xlsx', sheet_name='Sheet1')
# df6 = pd.read_excel('E 생활서비스(11,087).xlsx', sheet_name='Sheet1')
# df7 = pd.read_excel('G 숙박업(7,113).xlsx', sheet_name='Sheet1')
# df8 = pd.read_excel('H 관광여가오락(4,949).xlsx', sheet_name='Sheet1')
df = pd.read_csv('kor_Pair_test.csv', sep = ',', encoding= 'utf-8')
df2 = pd.read_csv('kor_pair_train.csv', sep = ',', encoding= 'utf-8')
df3 = pd.read_csv('./csv/movie.csv', sep = ',', encoding= 'utf-8')

input_file='corpus2.txt'


with open(input_file, 'a+', encoding='utf-8') as f:
    for index, row in df3.iterrows():
        f.write('{}\n'.format(row['review']))
  
        
      
# result = pd.concat([df1, df2])
# result2 = pd.concat([df3, df4])
# result3 = pd.concat([df5, df6])
# result4 = pd.concat([df7, df8])

# test1 = pd.concat([result, result2])
# test2 = pd.concat([result3, result4])

# data = pd.concat([test1,test2])

# tagger =Mecab()

# print(df.head(20))

# text1 = '감사합니다 앞으로도 잘부탁드려요 풍성한토핑 맛난피자로 보답하겠습니다'
# text2 = '맛있게 잘 먹었습니다~'
# text3 = '마시써효!!!떡볶이도좋아요'
# text4 = '불고기는 처음 시켜봤는데 상상 그이상....'
# text5 = '냠냠~너무 맛있어용^^ 또 시켜먹어요넘나맛있네여피짜로덤왜인기가잇는지알겟둠원픽예약임툐쿄'
# text6 = '영등포피자중 이찌방'
# text7 = 'ㅋㅋㅋㅋ 파인애플 당연 추가한줄알고 실수했네요죄송염~~🤣🤣오늘도 맛나게 잘 먹겠습니다^^🥰샐러드가 생각보다 푸짐하게 왔네요🥰'
# print(tagger.pos(text1))
# print(tagger.pos(text2))
# print(tagger.pos(text3))
# print(tagger.pos(text4))
# print(tagger.pos(text5))
# print(tagger.pos(text6))
# print(tagger.pos(text7))

# 띄어쓰기
# [('감사', 'NNG'), ('합니다', 'XSV+EF'), ('앞', 'NNG'), ('으로', 'JKB'), ('도', 'JX'), ('잘', 'MAG'), ('부탁', 'NNG'), ('드려요', 'VV+EC'), ('풍성', 'XR'), ('한', 'XSA+ETM'), ('토핑', 'NNG'), ('맛난', 'VA+ETM'), ('피자', 'NNG'), ('로', 'JKB'), ('보답', 'NNG'), ('하', 'XSV'), ('겠', 'EP'), ('습니다', 'EF')]
# [('맛있', 'VA'), ('게', 'EC'), ('잘', 'MAG'), ('먹', 'VV'), ('었', 'EP'), ('습니다', 'EF'), ('~', 'SY')]
# [('마시', 'NNG'), ('써', 'VV+EC'), ('효', 'NNG'), ('!', 'SF'), ('!!', 'SY'), ('떡볶이', 'NNG'), ('도', 'JX'), ('좋', 'VA'), ('아요', 'EC')]
# [('불고기', 'NNG'), ('는', 'JX'), ('처음', 'NNG'), ('시켜', 'XSV+EC'), ('봤', 'VX+EP'), ('는데', 'EC'), ('상상', 'NNG'), ('그', 'MM'), ('이상', 'NNG'), ('.', 'SF'), ('...', 'SY')]
# [('냠냠', 'MAG'), ('~', 'SY'), ('너무', 'MAG'), ('맛있', 'VA'), ('어용', 'EC'), ('^^', 'SY'), ('또', 'MAG'), ('시켜', 'VV+EC'), ('먹', 'VV'), ('어요', 'EF'), ('넘', 'VV'), ('나', 'EC'), ('맛있', 'VA'), ('네', 'EF'), ('여피', 'NNG'), ('짜', 'XSN'), ('로', 'JKB'), ('덤', 'NNG'), ('왜', 'MAG'), ('인기', 'NNG'), ('가', 'JKS'), ('잇', 'VV'), ('는지
# ', 'EC'), ('알', 'VV'), ('겟', 'EC'), ('둠', 'VX+ETN'), ('원', 'NNG'), ('픽', 'NNG'), ('예약', 'NNG'), ('임', 'VCP+ETN'), ('툐쿄', 'UNKNOWN')]
# [('영등포', 'NNP'), ('피자', 'NNG'), ('중', 'NNB'), ('이', 'JKS'), ('찌', 'MAG'), ('방', 'NNG')]
# [('ㅋㅋ', 'IC'), ('ㅋㅋ', 'IC'), ('파인애플', 'NNG'), ('당연', 'NNG'), ('추가', 'NNG'), ('한', 'XSA+ETM'), ('줄', 'NNB'), ('알', 'VV'), ('고', 'EC'), ('실수', 'NNG'), ('했', 'XSV+EP'), ('네요', 'EF'), ('죄', 'NNG'), ('송염', 'NNP'), ('~~', 'SY'), ('��🤣🤣', 'SY'),(오오늘늘', 'NNG'),('도도', 'JX'),(맛맛나나', 'VA'),('게게', 'EC'),('잘잘', 'MAG'),('
#  'VV'), ('겠', 'EP'), ('습니다', 'EF'), ('^^', 'SY'), ('🥰', 'SY'), ('샐러드', 'NNG'), ('가', 'JKS'), ('생각',  'NN'), ('보다', 'JKB'), ('푸짐', 'XR'), ('하', 'XSA'), ('게', 'EC'), ('왔', 'VX+EP'), ('네요', 'EF'), ('🥰', 'SY ')]  

# ===========================================Sentencepiece =====================================

#print(df1.head(20))

# input_file = './csv/corpus.txt'

# # 텍스트 파일로 만들기 -> setencepiece는 txt만 받음
# with open(input_file, 'a+', encoding='utf-8') as f:
#     for index, row in data.iterrows():
#         f.write('{}\n'.format(row['SENTENCE']))
#         # if row['CATEGORY'] == '배달음식점':
#         #     f.write ('{}\n'.format(row['SENTENCE']))


# parameter = '--input={} --model_prefix={} --vocab_size={} --user_defined_symbols={}'

# input_file = './csv/corpus.txt'
# vocab_size = 12510 #3,2000이 가장 좋으나 할 수가 없음ㅠ
# prefix = 'test' #'bert_kor'
# user_defined_symbols = '[PAD],[UNK],[CLS],[SEP],[MASK]'
# model_type = 'bpe'

# cmd = parameter.format(input_file, prefix, vocab_size, user_defined_symbols)

# spm.SentencePieceTrainer.Train(cmd)


# sp = spm.SentencePieceProcessor()
# sp.Load('{}.model'.format(prefix)) 
# token = sp.EncodeAsPieces(text1) #['▁감사합니다', '▁', '앞', '으로', '도', '▁잘', '부', '탁', '드려요', '▁', '풍', '성', '한', '토핑', '▁맛', '난', '피자', '로', '▁보', '답', '하겠습니다']
# token2 = sp.EncodeAsPieces(text2) #['▁맛있', '게', '▁잘', '▁먹', '었', '습니다', '~']
# token3 = sp.EncodeAsPieces(text3) #['▁마', '시', '써', '효', '!', '!', '!', '떡', '볶', '이', '도', '좋', '아요']
# token4 = sp.EncodeAsPieces(text4) #['▁불고기', '는', '▁', '처', '음', '▁시켜', '봤', '는데', '▁상', '상', '▁그', '이상', '.', '.', '.', '.']
# token5 = sp.EncodeAsPieces(text5) #['▁', '냠냠', '~', '너', '무', '▁맛있', '어', '용', '^^', '▁', '또', '▁시켜', '먹', '어요', '넘', '나', '맛', '있', '네', '여', '피', '짜', '로', '덤', '왜', '인', '기가', '잇', '는', '지', '알', '겟둠', '원', '픽', '예', '약', '임', '툐쿄']
# token6 = sp.EncodeAsPieces(text6) #['▁', '영', '등', '포', '피자', '중', '▁이', '찌', '방']
# token7 = sp.EncodeAsPieces(text7) 

# ['▁감사합니다', '▁앞', '으로', '도', '▁잘', '부탁드려요', '▁', '풍', '성', '한', '토핑', '▁맛', '난', '피자', '로', '▁보', '답', '하겠습니다']
# ['▁맛있게', '▁잘', '▁먹었', '습니다', '~']
# ['▁마시', '써', '효', '!', '!', '!', '떡볶이', '도', '좋', '아요']
# ['▁불고기', '는', '▁처음', '▁시켜', '봤', '는데', '▁상', '상', '▁그', '이상', '.', '.', '.', '.']
# ['▁', '냠냠', '~', '너', '무', '▁맛있어', '용', '^^', '▁', '또', '▁시켜', '먹어요', '넘', '나', '맛', '있', '네', '여', '피', '짜', '로', '덤', '왜', '인', '기가', '잇', '는', '지', '알', '겟', '둠', '원', '픽
# ', '예약', '임', '툐쿄']
# ['▁영', '등', '포', '피자', '중', '▁이', '찌', '방']

'''
['▁감사합니다', '▁앞으로', '도', '▁잘', '부탁드려요', '▁풍성', '한', '토핑', '▁맛', '난', '피자', '로', '▁보', '답', '하겠습니다']
['▁맛있게', '▁잘', '▁먹었', '습니다', '~']
['▁마시', '써', '효', '!', '!', '!', '떡볶이', '도', '좋아요']
['▁불고기', '는', '▁처음', '▁시켜', '봤는데', '▁상', '상', '▁그', '이상', '.', '.', '.', '.']
['▁', '냠냠', '~', '너', '무', '▁맛있어', '용', '^^', '▁또', '▁시켜먹', '어요', '넘', '나', '맛', '있', '네', '여', '피', '짜', '로', '덤', '왜', '인', '기가', '잇', '는', '지', '알', '겟', '둠', '원', '픽', '예약', '임', '툐쿄']
['▁영', '등', '포', '피자', '중', '▁이', '찌', '방']
['▁', 'ᄏᄏᄏᄏ', '▁파인애플', '▁당연', '▁추가', '한', '줄', '알', '고', '▁실수', '했', '네요', '죄', '송', '염', '~', '~', '��🤣🤣' 오오늘늘' '도도','▁맛맛' '나나' '게게','▁잘잘','▁먹먹' 겠습니니다다', '^^🥰,'샐러러드 각', '보다', '▁푸', '짐', '하게', '▁왔', '네요', '🥰']
'가', '▁생각', '보다', '▁푸', '짐', '하게', '▁왔', '네요', '🥰']




['▁감사합니다', '▁앞으로', '도', '▁잘', '부탁드려요', '▁풍성', '한', '토핑', '▁맛', '난', '피자', '로', '▁보', '답', '하겠습니다']
['▁맛있게', '▁잘', '▁먹', '었', '습니다', '~']
['▁마시', '써', '효', '!', '!', '!', '떡볶이', '도', '좋', '아요']
['▁불고기', '는', '▁처음', '▁시켜', '봤는데', '▁상', '상', '▁그', '이상', '.', '.', '.', '.']
['▁', '냠냠', '~', '너', '무', '▁맛있어', '용', '^^', '▁또', '▁', '시켜먹어', '요', '넘', '나', '맛', '있', '네', '여', '피', '짜', '로', '덤', '왜', '인', '기가', '잇', '는', '지', '알', '겟', '둠', '원', '픽
', '예약', '임', '툐쿄']
['▁영', '등', '포', '피자', '중', '▁이', '찌', '방']
['▁', 'ᄏᄏᄏᄏ', '▁파인애플', '▁당', '연', '▁추가', '한', '줄', '알', '고', '▁실', '수', '했', '네요', '죄', '송', '염', '~', '~', '��🤣🤣' '오오' '늘늘' '도도','▁맛맛' '나나' '게게','▁잘잘','▁먹먹' 겠습니니다다', '^', '가', '▁생각', '보다', '▁', '푸', '짐', '하게', '▁왔', '네요', '🥰']
, '샐러드', '가', '▁생각', '보다', '▁', '푸', '짐', '하게', '▁왔', '네요', '🥰']


'''

# print(token)
# print(token2)
# print(token3)
# print(token4)
# print(token5)
# print(token6)
# print(token7)

'''
input_file : 내 한국어 데이터 경로를 지정한다.
vocab_size : BPE의 단어수를 얼마로 할 것인가 이다. 너무 적으면 한 글자 단위로 쪼개지는 경향이 있고, 너무 많으면 쓸데없는 단어들이 만들어진다. 주로 3,2000이 가장 좋다고 알려져 있다.
model_name : 저장할 이름이다. 학습하고 나면 <model_name>.model, <model_name>.vocab 2개의 파일이 만들어진다.
model_type : bpe, unigram 등이 있는데 두가지를 모두 사용해 보고 성능이 좋은 거로 고르도록 하자. 
character_coverage : 모든 단어를 커버할것인가, 너무 희귀한 단어는 뺄 것인가 이다. 학습 코퍼스가 대용량이라면 보통 0.9995로 사용하면 된다. 그런데 코퍼스가 작다면 1.0으로 지정하자. 그럼 [UNK]가 없다.
user_defined_symbols : BPE로 생성된 단어 외 알고리즘에서 사용할 특수문자들을 지정한다.
'''
# input_file = './csv/corpus.txt'
# vocab_size = 12524
# model_name = 'model_sentencepiece/sentencepiece_tokenizer_kor_%d' % (vocab_size)
# model_type = 'bpe'
# character_coverage  = 1.0  # 0.9995
# user_defined_symbols = '[PAD],[UNK],[CLS],[SEP],[MASK],[BOS],[EOS],[UNK0],[UNK1],[UNK2],[UNK3],[UNK4],[UNK5],[UNK6],[UNK7],[UNK8],[UNK9],[unused0],[unused1],[unused2],[unused3],[unused4],[unused5],[unused6],[unused7],[unused8],[unused9],[unused10],[unused11],[unused12],[unused13],[unused14],[unused15],[unused16],[unused17],[unused18],[unused19],[unused20],[unused21],[unused22],[unused23],[unused24],[unused25],[unused26],[unused27],[unused28],[unused29],[unused30],[unused31],[unused32],[unused33],[unused34],[unused35],[unused36],[unused37],[unused38],[unused39],[unused40],[unused41],[unused42],[unused43],[unused44],[unused45],[unused46],[unused47],[unused48],[unused49],[unused50],[unused51],[unused52],[unused53],[unused54],[unused55],[unused56],[unused57],[unused58],[unused59],[unused60],[unused61],[unused62],[unused63],[unused64],[unused65],[unused66],[unused67],[unused68],[unused69],[unused70],[unused71],[unused72],[unused73],[unused74],[unused75],[unused76],[unused77],[unused78],[unused79],[unused80],[unused81],[unused82],[unused83],[unused84],[unused85],[unused86],[unused87],[unused88],[unused89],[unused90],[unused91],[unused92],[unused93],[unused94],[unused95],[unused96],[unused97],[unused98],[unused99]'

# input_argument = '--input=%s --model_prefix=%s --vocab_size=%s --user_defined_symbols=%s --model_type=%s --character_coverage=%s'
# cmd1 = input_argument%(input_file, model_name, vocab_size,user_defined_symbols, model_type, character_coverage)

# spm.SentencePieceTrainer.Train(cmd1)
# print('train done')
 

# sp = spm.SentencePieceProcessor()
# sp.Load('{}.model'.format(model_name))
# sentencepiece_tokenizer = sp.encode
# token = sentencepiece_tokenizer(text1, out_type=str)

# print(token)