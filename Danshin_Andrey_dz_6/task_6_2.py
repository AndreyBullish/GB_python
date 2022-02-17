import requests
from pprint import pprint


response = requests.get('https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs')
web_text = response.text
with open('nginx_logs.txt', 'w', encoding='utf-8') as fw:
     fw.writelines(web_text)
def get_parse_attrs(line: str) -> tuple:
    remote_addr = line.rpartition(' - - ')[0]
    return remote_addr

ip_list = list()
file_1 = open('nginx_logs.txt', 'r', encoding='utf-8')
for line in file_1:
    ip_list.append(get_parse_attrs(line))
file_1.close()

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
#программа выполняется 3 мин, @Анатолий, подскажите как можно ускорить? или надо было делать не через отдельный список и словарь
print(f'ip спамера = {ip_spamer_print}, кол-во запросов = {ip_spamer_count}')
print('\n''end')

#я не понял как выполнить данный момент - код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера. ПОДСКАЖИТЕ, ПОЖАЛУЙСТА