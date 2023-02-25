import re

s = 'Привет! Как дела? А у меня нормально.'
result = re.search(r'[бБвВгГдДжЖзЗкКлЛмМнНпПрРсСтТфФхХцЦчЧшШщЩ]\w+', s)

print(result.group())
