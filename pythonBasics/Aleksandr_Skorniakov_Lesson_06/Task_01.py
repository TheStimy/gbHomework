from re import findall

with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    nginx_logs = f.read()

text = nginx_logs.split('\n')

for string in text:
    ip_address = str(findall(r'\d+.\d+.\d+.\d+ -', string))[2:-4]
    method = str(findall(r'"\w+ /', string))[3:-4]
    path = str(findall(r'/\w+/\w+ ', string))[2:-3]
    message = ip_address, method, path
    print(tuple(message))
