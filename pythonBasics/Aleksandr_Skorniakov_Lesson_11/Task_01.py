import re


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def str_to_int(cls, date):
        split_data = re.split(r'\D+', date)
        year, month, day = int(split_data[0]), int(split_data[1]), int(split_data[2])
        return cls(year, month, day)

    @staticmethod
    def check_date(obj):
        print('Year is correct') if 1900 < obj.year < 2021 else print('pass')
        print('Month is correct') if 0 < obj.month < 13 else print('pass')
        print('Day is correct') if 0 < obj.day < 32 else print('pass')


date_01 = Date.str_to_int('1990-12-27')
date_01.check_date(date_01)
