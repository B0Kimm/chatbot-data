from soyspacing.countbase import CountSpace
from soyspacing.countbase import RuleDict


corpus_fname = 'corpus.txt'
model = CountSpace()
model.train(corpus_fname)

# 모델을 저장
model_fname = 'ver1spacing.h5'
model.save_model(model_fname, json_format=False)

model = CountSpace()
model.load_model(model_fname, json_format=False)

rule_dict = RuleDict('rules.txt')

text1 = '감사합니다 앞으로도 잘부탁드려요 풍성한토핑 맛난피자로 보답하겠습니다'
text2 = '맛있게 잘 먹었습니다~'
text3 = '마시써효!!!떡볶이도좋아요'
text4 = '불고기는 처음 시켜봤는데 상상 그이상....'
text5 = '냠냠~너무 맛있어용^^ 또 시켜먹어요넘나맛있네여피짜로덤왜인기가잇는지알겟둠원픽예약임툐쿄'
text6 = '영등포피자중 이찌방'
text7 = 'ㅋㅋㅋㅋ 파인애플 당연 추가한줄알고 실수했네요죄송염~~오늘도 맛나게 잘 먹겠습니다^^샐러드가 생각보다 푸짐하게 왔네요'

sent_corrected, tags = model.correct(text1, rules=rule_dict)
sent_corrected2, tags = model.correct(text2, rules=rule_dict)
sent_corrected3, tags = model.correct(text3, rules=rule_dict)
sent_corrected4, tags = model.correct(text4, rules=rule_dict)
sent_corrected5, tags = model.correct(text5, rules=rule_dict)
sent_corrected6, tags = model.correct(text6, rules=rule_dict)
sent_corrected7, tags = model.correct(text7, rules=rule_dict)

print(sent_corrected)
print(sent_corrected2)
print(sent_corrected3)
print(sent_corrected4)
print(sent_corrected5)
print(sent_corrected6)
print(sent_corrected7)