# Вывести последнюю букву в слове
word = 'Архангельск'
print('Последняя буква:',word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'
a = word.lower()
print('Количество букв а:',a.count('а'))

# Вывести количество гласных букв в слове
word = 'Архангельск'
a = word.lower()
e = word.lower()
print('Всего гласных:',a.count('а') + e.count('е')) # 1 способ
count = 0 # 2 способ
for i in word.lower():
    if i == 'а' or i == 'е':
        count += 1
print('Всего гласных:',count)    

# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
words = 0
for i in sentence.split():
    if i in sentence:
        words += 1
print('Количество слов способ 1:',words)
sentence = sentence.split()
print('Количество слов способ 2:',len(sentence))

# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
for words in sentence.split():
    print(words[0])


# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'
string_len = len(sentence) / 4
print(string_len)
