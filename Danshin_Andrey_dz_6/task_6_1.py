import requests
from pprint import pprint


response = requests.get('https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs')
print(response)
web_text = response.text

with open('nginx_logs.txt', 'w', encoding='utf-8') as fw:
     fw.writelines(web_text)
def get_parse_attrs(line: str) -> tuple:
    remote_addr = row.rpartition(' - - ')[0]
    request_type_start = row.find('+0000]') + 8
    request_type_end = row.find('/downloads')
    request_type = row[request_type_start:request_type_end]
    requested_resource_start = row.find('/downloads')
    requested_resource_end = row.find('HTTP/')
    requested_resource = row[requested_resource_start:requested_resource_end]
    result = remote_addr, request_type, requested_resource
    return result

list_out = list()
with open('nginx_logs.txt', 'r', encoding='utf-8') as fr:
    for row in fr:
        list_out.append(get_parse_attrs(row))

pprint(list_out)

print('\n''end')