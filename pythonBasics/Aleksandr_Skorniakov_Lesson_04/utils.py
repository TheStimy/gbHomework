from requests import get, utils
from datetime import datetime
from re import findall

data = utils.get_unicode_from_response(get('http://www.cbr.ru/scripts/XML_daily.asp')).split('Valute')


def currency_rates(currency_input):
    flag = 0

    date = str(findall(r'\d\d.\d\d.\d{4}', data[0])).split('.')
    currency_date = datetime(year=int(date[2][:4]), month=int(date[1]), day=int(date[0][2:]))

    for string in data:
        if currency_input.upper() in string:
            print(float(string[string.find('<Value>') + 7:string.find('</Value>')].replace(',', '.')),
                  currency_date.date())
            flag = 1

    if flag == 0:
        print(None)


if __name__ == '__main__':
    currency_rates(input('Enter currency: '))
