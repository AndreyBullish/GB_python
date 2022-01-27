def convert_time(duration):
    if duration < 60:
        return f'{duration} сек'
    if duration >= 60 and duration < 3600:
        min = duration//60
        sec = duration%60
        return f'{min} мин {sec} сек'
    if duration >= 3600 and duration < 86400:
        hours = duration // 3600
        min = (duration-(hours*3600))//60
        sec = duration % 60
        return f'{hours} час {min} мин {sec} сек'
    if duration >= (60 * 60 * 24):
        days = duration // (60 * 60 * 24)
        hours = (duration-(days*86400))//3600
        min = (duration - ((days*86400)+(hours*3600)))//60
        sec = duration % 60
        return f'{days} дн {hours} час {min} мин {sec} сек'
duration = 400153
result = convert_time(duration)
print(result)
print('end')
#я совсем не понял, что имелось ввиду в конце задания, тут - можно ли использовать цикл для проверки работы кода сразу для нескольких значений продолжительности, будет ли тут полезен список?
#расскажите, пжл, по возможности