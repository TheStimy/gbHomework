from requests import get, utils

data = utils.get_unicode_from_response(get('http://www.cbr.ru/scripts/XML_daily.asp')).split('Valute')

flag = 0
currency_input = input('Enter currency: ')

for string in data:
    if currency_input.upper() in string:
        print(float(string[string.find('<Value>') + 7:string.find('</Value>')].replace(',', '.')))
        flag = 1

if flag == 0:
    print(None)
