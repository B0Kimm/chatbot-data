import pandas as pd
import pandas as pd

filename = 'test.csv'
review = './csv/review.csv'

myframe = pd.read_csv(filename, sep = ',', encoding= 'utf-8')
myreview = pd.read_csv(review, sep = ',', encoding= 'utf-8')

# myframe = myframe.dropna(axis=0)

# print(myreview.head(100))

        
# csvfilename = 'store.csv'
# myframe.to_csv(csvfilename, mode= 'w', encoding='utf-8',index=False)
# print(f'--------{csvfilename} done -------------')


new_myframe = pd.DataFrame(myframe.address.str.split(' ').tolist())
columns = ['시', '구', '동', '지번','상세']

result = []
for index, row in new_myframe.iterrows():
    imsi = [row[0], row[1], row[2],row[3], row[4]]
    result.append(imsi)

result = pd.DataFrame(result, columns=columns)

print(result.head(10))

data = pd.concat([myframe, result],axis=1)
print(data.head(20))

outcome=[]
review_columns = ['id', 'nickname','orderid','menu_summary', 'comment']
for index, row in myreview.iterrows():
    imsi = [row['storeid'], row['nickname'], row['customerid'],row['menu_summary'], row['comment']]
    outcome.append(imsi)

# outcome = pd.DataFrame(outcome, columns= review_columns)
# # merge는 같은 indext, join은 merge와 비슷
data = pd.merge(myframe, result, on='id', how='left')
data = myframe.join(result)

# mergedata = pd.merge(data, outcome, on='id', how='left')

# print(mergedata.head())
# filename2='test3.csv'
# mergedata.to_csv(filename2, mode='w', encoding='utf-8', index=False)


# # outputname = 'new_data.csv'
# # data.to_csv(outputname, mode='w', encoding='utf-8', index=False)

