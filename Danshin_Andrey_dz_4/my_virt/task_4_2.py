import requests


def currency_rates(code: str) -> float:
    """возвращает курс валюты `code` по отношению к рублю"""
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    code = code.upper()
    response = requests.get(url)
    cur = response.text
    start_index = cur.find(code)

    if cur.find(code) == -1:
        return None
    else:
        nominal_first_cut = cur[start_index:cur.find('</Nominal>', start_index)]
        nominal_second_cut = nominal_first_cut.find('<Nominal>') + len('<Nominal>')
        nominal_value = int(nominal_first_cut[nominal_second_cut:])
        if nominal_value == 1:
            first_cut = cur[start_index:cur.find('</Value', start_index)]
            second_cut = first_cut.find('<Value') + len('<Value>')
            result_value = first_cut[second_cut:]
            result_value = float(result_value.replace(',', '.'))
            result_value = float('{0:.2f}'.format(result_value))
            return result_value
        else:
            first_cut = cur[start_index:cur.find('</Value', start_index)]
            second_cut = first_cut.find('<Value') + len('<Value>')
            result_value = first_cut[second_cut:]
            result_value = float(result_value.replace(',', '.'))
            result_value = (float('{0:.2f}'.format(result_value)))/nominal_value
            return result_value

print(currency_rates("USD"))
print(currency_rates("AMD"))
print(currency_rates("None"))


print('\n','end')



