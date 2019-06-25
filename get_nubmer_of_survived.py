# импорт необходимых библиотек для работы
import pandas as pd

def percentage(perc, whole):
    return (perc * 100) / whole


def get_nubmer_of_survived(data = None):
    survived = data.value_counts()
    died_int = survived[0]
    surv_int = survived[1]
    return percentage(surv_int, surv_int+died_int)

data = pd.read_csv('train.csv', index_col='PassengerId')

surv_int = get_nubmer_of_survived(data['Survived'])
print(surv_int)

