import requests  # Импорт библиотеки для запросов к серверу
from bs4 import BeautifulSoup # Импорт библиотеки для автоматического парсинга странички
import json

#URL = 'https://health-diet.ru/table_calorie/'
#req = requests.get(URL)  # GET-запрос
#print(req.text)

#with open('index.html', 'w') as file:
#    file.write(req.text)
#print(file)


# with open('index.html') as file:
#     scr = file.read()
#print(scr)

# soup = BeautifulSoup(scr, 'lxml')
# categories = soup.find_all(class_='mzr-tc-group-item-href')

# all_categories_dict = {}
# for name in categories:
#     all_categories_dict[name.text] = 'https://health-diet.ru' \
#                                      + name.get('href')
#
# #print(all_categories_dict)
#
# with open('all_categories.json', 'w') as file:
#     json.dump(all_categories_dict, file, indent='', ensure_ascii=False)

with open('all_categories.json') as file:
    all_categories = json.load(file)

symbols = ['-', ', ',' ', "'"]
count = 0

for cat_name, link in all_categories.items():
    if count == 0:
        for sym in symbols:
            if sym in cat_name:
                cat_name = cat_name.replace(sym, '_')
                print(cat_name)

        request = requests.get(link)
        src = request.text
        with open(f'data/{count}_{cat_name}.html', 'w') as file:
            file.write(src)
            print(f'file {count}_{cat_name}.html created' )
        count+=1