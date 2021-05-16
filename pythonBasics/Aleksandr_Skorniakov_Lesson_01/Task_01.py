duration_list = [
    53,
    153,
    4153,
    400153
]

for duration in duration_list:
    seconds = duration % 60
    minutes = duration % 86400 % 3600 // 60
    hours = duration % 86400 // 3600
    days = duration // 86400
    print(f'{days} дн. {hours} ч. {minutes} мин. {seconds} сек.')
