import numpy as np
import pandas as pd


data = pd.read_csv('train.csv', index_col='PassengerId')

age_arr = data['Age']
survived_arr = data['Survived']

sex_arr = data['Sex']
#survived_arr = data['Survived']

pclass_arr = data['Pclass']
#survived_arr = data['Survived']

one_pearson_int = np.corrcoef(age_arr, survived_arr)

#two_pearson_int = np.corrcoef(sex_arr, survived_arr)

tree_pearson_int = np.corrcoef(pclass_arr,survived_arr)

#ages_lst = data['Age'].value_counts().index.tolist()

#sex_lst = data['Sex'].value_counts().index.tolist()

#pclass_lst = data['Pclass'].value_counts().index.tolist()

print(one_pearson_int)

#print(two_pearson_int)

print(tree_pearson_int)


