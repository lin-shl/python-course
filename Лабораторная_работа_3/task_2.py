def find_common_participants(first, second, splitter=','):
    common = list(set(first.split(splitter)).intersection(second.split(splitter)))
    common.sort()

    return common

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, '|'))