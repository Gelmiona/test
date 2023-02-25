quotes=[(1, 'Rick Cook', 'Программирование сегодня — это гонка разработчиков программ...'),
        (2, 'Waldi Ravens', 'Программирование на С похоже на быстрые танцы на только...'),
        (3, 'Rick Cook', 'Программирование сегодня — это гонка разработчиков программ...'),
        (4, 'Waldi Ravens', 'Программирование на С похоже на быстрые танцы на только...'),
        (5, 'Rick Cook', 'Программирование сегодня — это гонка разработчиков программ...'),
        (6, 'Waldi Ravens', 'Программирование на С похоже на быстрые танцы на только...'),
        (7, 'test1', 'Программирование сегодня — это гонка разработчиков программ...'),
        (8, 'test2', 'Программирование на С похоже на быстрые танцы на только...')]

# keys = ['id','author','text']
# quotes_dict=[]
# for i in quotes:
#     quotes_dict.append(dict((zip(keys, quotes[0]))))
# print(quotes_dict)

#v2 более частный случай
def convert_data(quotes: tuple)->dict:
    keys = ["id", "author", "text"]
    res=[]
    for quote in quotes:
        res.append(dict(zip(keys, quote)))
    return res
print(convert_data(quotes))