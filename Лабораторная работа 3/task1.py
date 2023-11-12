# TODO Напишите функцию для поиска индекса товара
def find(list_, product):
    if product not in list_:
        return None
    else:
        index = 0
        a = list_[index]
        while a != product:
            index += 1
            a = list_[index]
        return index

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = find(items_list,find_item)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
