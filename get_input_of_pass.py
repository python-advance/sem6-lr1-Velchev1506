import pandas as pd

data = None
def percentage(perc, whole):
	return (perc * 100) / whole

def get_input_of_pass(embarked, data = None):
	# Подсчитайте сколько пассажиров загрузилось на борт в различных портах?
	#Приведите два числа через пробел
	
	embarkedratio = data.value_counts()

	if embarked == 's':
		return embarkedratio['S']
	elif embarked == 'c':
		return embarkedratio['C']
	elif embarked == 'q':
		return embarkedratio['Q']

data = pd.read_csv('train.csv', index_col="PassengerId" )
#print(data['S'])
s_int = input_of_pass('s', data['Embarked'] )
c_int = input_of_pass('c', data['Embarked'] )
q_int = input_of_pass('q', data['Embarked'] )

#print (S_int, C_int, Q_int)
port_int = s_int + c_int +q_int
print (round(percentage(s_int, port_int)), round(percentage(c_int, port_int)), round(q_int, port_int)) 
