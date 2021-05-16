for number in range(-30, 31):
    if abs(number) % 10 == 1 and abs(number) % 100 != 11:
        print(f'{number} процент')
    elif 5 <= abs(number) % 10 <= 10 or 11 <= abs(number) % 100 <= 14 or number % 10 == 0:
        print(f'{number} процентов')
    else:
        print(f'{number} процента')
