import requests
from pprint import pprint


response = requests.get('https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs')
web_text = response.text
with open('nginx_logs.txt', 'w', encoding='utf-8') as fw:
     fw.writelines(web_text)
def get_parse_attrs(line: str) -> tuple:
    remote_addr = row.rpartition(' - - ')[0]
    return remote_addr

ip_list = list()
with open('nginx_logs.txt', 'r', encoding='utf-8') as fr:
    for row in fr:
        ip_list.append(get_parse_attrs(row))

ip_count_list = []
for i in ip_list:
    ip_count_list.append(ip_list.count(i))
    ip_spamer_count = max(ip_count_list)
    dict_ip_count_list = dict(zip(ip_list, ip_count_list))

def get_key(dict, value):
    for k, v in dict_ip_count_list.items():
        if v == value:
            return k
ip_spamer_print = get_key(dict_ip_count_list, ip_spamer_count)
print(f'ip спамера = {ip_spamer_print}, кол-во запросов = {ip_spamer_count}')
print('\n''end')

