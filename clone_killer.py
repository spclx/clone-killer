import json

data=[]
#открытие файла с упоминаемыми персонами
with open("/Users/spacelexey/OneDrive/mentioned_people.json", "r") as read_file:
    data = json.load(read_file)

#получение словаря id : строка с именем ФИО для сортировки...
names = {}
#...и словаря со всей служебной информации для последующего вывода
cards = {}

for i in data:
    names[i['id']] = '"' + i["firstName"] + '" "' + i["lastName"] + '" "' + i["thirdName"] + '"'
    cards[i['id']] = [i["firstName"], i["lastName"], i["thirdName"], i["nickname"], 
        i["birthDay"], i["deathDay"], i["comment"]]

#поиск повторяющихся значений
rev_dict = {}

for key, value in names.items():
    rev_dict.setdefault(value, set()).add(key)

#здесь будут храниться ключи повторяюшихся элементов
cloneKeys = filter(lambda x: len(x)>1, rev_dict.values())

#интерактивный инструмент по отбору
#в строку clones будет записываться информация об id дублей и оригиналов для последующего вывода в файл
clones = ""

for clonePair in list(cloneKeys):
    s = ""
    for item in clonePair:

        s += """
        ===================
        id =            {id}
        Фамилия =       {lastName}
        Имя =           {firstName}
        Отчество =      {thirdName}
        Др.имя =        {nickname}
        Даты =          {birthDay} - {deathDay}
        Комментарий =   {comment}
        ====================
        """.format(id = item, firstName = cards[item][0], lastName = cards[item][1], 
            thirdName = cards[item][2], nickname = cards[item][3],
            birthDay = cards[item][4], deathDay = cards[item][5], comment = cards[item][6])
    s += """
    Это карточки об одном человеке?
    1) Да 2) Нет 3) Не уверен
    """
    print(s)
    answer1 = int(input())
    if answer1 == 1 :
        print("Какая карточка наиболее полная?")
        answer2 = int(input())
        clones += str(list(clonePair)) + " original: " + list(clonePair)[answer2 - 1] + '\n'
    elif answer1 == 2:
        continue
    elif answer1 == 3:
        clones += str(list(clonePair)) +  " original: Check! " + '\n'

#запись всех клонов в файл
#вывод: {id клонов} original: [id оригинала]
cloneFile = open('/Users/spacelexey/OneDrive/clones.txt', 'w')
cloneFile.write(clones)
cloneFile.close
