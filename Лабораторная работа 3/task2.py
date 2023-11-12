# TODO Напишите функцию find_common_participants
def find_common_participants(first_group, second_group, character = ","):
    first_set, second_set = set(first_group.split(character)), set(second_group.split(character))
    in_both_groups = list(first_set.intersection(second_set))
    in_both_groups.sort()
    return in_both_groups

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
print(find_common_participants(participants_first_group, participants_second_group, "|"))

# TODO Провеьте работу функции с разделителем отличным от запятой
