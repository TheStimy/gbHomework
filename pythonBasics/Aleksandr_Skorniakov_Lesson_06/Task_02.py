from re import findall

with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    nginx_logs = f.read()

text = nginx_logs.split('\n')
ip_address = []

for string in text:
    ip_address.append(findall(r'\d+.\d+.\d+.\d+ -', string))

print(str(max(ip_address, key=ip_address.count))[2:-4])
