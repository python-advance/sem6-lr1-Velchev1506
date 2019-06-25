# импорт необходимых библиотек для работы
import pandas as pd

def percentage(perc, whole):
    return (perc * 100) / whole


def get_nubmer_of_class(data = None):
	survived = data.value_counts()
	Pclass_int = survived[0]
	surv_int = survived[1]
	return percentage(Pclass_int, Pclass_int+surv_int)

data = pd.read_csv('train.csv', index_col='PassengerId')	

Pclass_int = get_nubmer_of_class(data['Survived'])
print(Pclass_int)
