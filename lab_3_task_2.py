# TODO Напишите функцию find_common_participants
def find_common_participants(str1, str2, separator=','):
    participants1 = str1.split(separator)
    participants2 = str2.split(separator)

    common_participants = sorted(set(participants1).intersection(set(participants2)))
    return common_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
common_participants = find_common_participants(participants_first_group, participants_second_group)
print(f"Общие участники: {common_participants}")