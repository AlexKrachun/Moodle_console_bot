from random import randint

topic_path = {
    '/1': 'cube',
    '/2': 'exponential',
    '/3': 'irrational',
    '/4': 'logarithmic',
}

kind_path = {
    '/1': 'equations',
    '/2': 'inequalities',
    '/3': 'expressions',
}


def create_task_file(data):
    topic = data['topic']
    kind = data['kind']
    amount = int(data['amount'][1:])
    path = f'./db/{topic_path[topic]}/{topic_path[topic]}_{kind_path[kind]}.txt'
    bd_file = open(path, encoding='utf-8')
    bd = [i for i in bd_file.read().split('\n\n')]
    bd_file.close()

    ind = randint(0, len(bd) - amount)
    tasks = bd[ind:ind + amount]

    for i in range(len(tasks)):
        a = tasks[i].split('::')
        a[1] = f' Вопрос {i + 1} \n'
        print('::' + '::'.join(a[1:]), end='\n\n')



print('''
Темы:
1. кубические
2. показательные
3. иррациональные
4. логарифмические


Виды 
1. уравнения
2. неравенства
3. вычислить
''')
topic = '/' + input('Выберете номер темы: ')
kind = '/' + input('Выберете номер вида: ')
amount = '/' + input('Ведите количество номеров до 1000: ')
data = {
    'topic': topic,
    'kind': kind,
    'amount': amount,
}
create_task_file(data)












