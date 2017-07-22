import numpy as np
input_values = [1,0]

wideness = 2#нужная ширина нейронки
length = 3# на сколько она будет глубкая 
weights = []
values = []

for each in range(length):
	weights.append(np.random.normal(0.5, 0.2, (wideness,wideness)))##заполняет список нампаевскими матрицами, которые используются как веса
	#без цикла это один слой. цикл создает их сколько указано
    #(wideness,wideness)первое значение - количество нейронов в этом слое. второе-в предыдущим, с которым этот связан.(x,y)
    #те строка это нейрон, а значения в нем, это веса.
for each in range(length):
	values.append(np.random.normal(0.5, 0.2, (wideness,1)))#тоже, но для значений. можно было создать пустые, но так проще

#следующий цикл нужен для заполнения самого первого эдемента в списке значений входными значениями... переводит список в список списков для нампая
i=[]
for each in input_values:
    i.append([each])
values.insert(0, np.array(i))

#активационная функция - сигмойййд
def sigmoid (x):
	return 1/(1+np.exp(-x))

# применяет активационную функцию к каждому слою
def use_activation(neuron_input):
	try:
		output_of_neuron = np.array([sigmoid(x) for x in neuron_input])
	except: 
		output_of_neuron = sigmoid(neuron_input)#это потому, что одно значение не итерируется
	return (output_of_neuron)

#эта функция умножает веса на входные значения
def multyplier(weights, inputs):
	new_input = np.dot(weights, inputs)#дот умножает матрицы, как они должны умножаться а потом всё это складывает
	outputs = use_activation(new_input)#применяет активационную
	return(outputs)

counter = 0#нужен потому, что мы вставили входные значения первыми
for each_layer in range(length):#цикл применяет математику к всей нейронной сети
	value = multyplier(weights[counter], values[counter])#отправляет поэлементно  значения в нампай
	counter+=1
	values[counter]=value# записывает полученное значение в список 
	print(counter)
	print('values')
	print(str(values))
#	print('weights')
#	print(str(weights))
