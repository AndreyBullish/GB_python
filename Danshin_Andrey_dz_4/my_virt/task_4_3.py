import requests
import datetime


def currency_rates_adv(code: str) -> float:
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
        date_value = cur[(cur.find('Date=')+6):cur.find('" name="Foreign Currency Market"')]
        year = int(date_value[6:])
        month = int(date_value[3:5])
        day = int(date_value[0:2])
        date = datetime.date(year, month, day)

        return result_value, date

        kurs, date_value = currency_rates_adv("USD")

print(currency_rates_adv("USD"))
print(currency_rates_adv("eur"))
print(currency_rates_adv("noname"))

kurs, date_value = currency_rates_adv("USD")

empty = bool(not kurs and not date_value)
if not empty and not isinstance(kurs, float):
    raise TypeError("Неверный тип данных у курса")
if not empty and not isinstance(date_value, datetime.date):
    raise TypeError("Неверный тип данных у даты")
print(kurs, date_value)

print('\n','end')
