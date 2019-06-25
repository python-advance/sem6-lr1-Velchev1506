import numpy as np
import pandas as pd

data = pd.read_csv('train.csv', index_col='PassengerId')

sibsp_arr = data['SibSp']
parch_arr = data['Parch']

pearson_int = np.corrcoef(sibsp_arr, parch_arr)

ages_lst = data['Age'].value_counts().index.tolist()
#print (type(age.value_counts().index.tolist()))
# print(age)

print(np.average(ages_lst))

#print(data.corr())
#print((pearson_int[0, 1]))