import pandas as pd
from pandas import DataFrame

review = './csv/review.csv'
food = './csv/menu.csv'
store = './csv/store.csv'
total ='total.csv'
category = 'category.csv'

myreview = pd.read_csv(review, sep = ',', encoding= 'utf-8')
myfood = pd.read_csv(food, sep = ',', encoding= 'utf-8')
mystore = pd.read_csv(store, sep = ',', encoding= 'utf-8')
data = pd.read_csv(total, sep = ',', encoding= 'utf-8')
mycategory = pd.read_csv(category, sep = ',', encoding= 'utf-8')



# myframe = pd.read_csv(mystore, sep = ',', encoding= 'utf-8')
columns = ['storeid','category']

# print(myframe['구'].value_counts(ascending=True))

result = []
for index, row in mystore.iterrows():
    imsi = [row['id'], row['categories']]
    result.append(imsi)



print(type(mycategory['category']))

categories = []
for list in mycategory['category'] :
    for item in list:
        if item not in categories:
            categories.append(item)

# mycategory = pd.DataFrame(mycategory.category.str.split(',').tolist())

# categories =[]
# for mycategory['category'] in mycategory:

#     for i in 
#         i not in categories:
#             categories.append(row['category'])

# mycategory = pd.DataFrame(mycategory, columns=columns)


categories = pd.DataFrame(categories, columns=columns)
categories.to_csv('categories.csv', mode='w', encoding='utf-8', index=False)

