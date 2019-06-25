# Решение

# импорт необходимых библиотек для работы
import pandas as pd

data = None
def percentage(perc, whole):
	return (perc * 100) / whole

def get_nubmer_of_pass(sex, data = None):
    """
        Какое количество мужчин и женщин ехало на параходе? 
        Приведите два числа через пробел
    """
    sexratio = data.value_counts()

    if sex == 'male':
        return sexratio['male']
    else:
        return sexratio['female']

data = pd.read_csv('train.csv', index_col='PassengerId')
#print(data['Sex'])
male_int = get_nubmer_of_pass('male', data['Sex'] )
female_int = get_nubmer_of_pass('female', data['Sex'])

#print (male_int, female_int)
total_int = male_int + female_int
print (round(percentage(male_int, total_int)), round(percentage(female_int, total_int)) )


		
























