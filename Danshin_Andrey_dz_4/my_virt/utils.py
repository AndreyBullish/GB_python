import requests


def currency_rates(code: str) -> float:
    """возвращает курс валюты `code` по отношению к рублю"""
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    code = code.upper()
    response = requests.get(url)
    cur = response.text
    if cur.find(code) == -1:
        return None
    else:
        start_index = cur.find(code)
        first_cut = cur[start_index:cur.find('</Value', start_index)]
        second_cut = first_cut.find('<Value') + len('<Value>')
        result_value = first_cut[second_cut:]
        result_value = float(result_value.replace(',', '.'))
        result_value = float('{0:.2f}'.format(result_value))
        return result_value

if __name__ == '__main__':
    print(currency_rates("USD"))
    print(currency_rates("eur"))
    print(currency_rates("noname"))

    print('\n', 'end')
