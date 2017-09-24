import time

# Получить Unix

print(int(time.time()))

# Конвертирование даты в Unix время

print(int(time.mktime(time.strptime('2000-01-01 12:34:00', '%Y-%m-%d %H:%M:%S'))))
# print(int(time.mktime(time.strptime('Sun, 24.09 17:12', '%a, %d.%m %H:%M'))))

# Конвертирование Unix времеми в понятную дату(human readable date)

# print(time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime()))
print(time.strftime("%a, %d.%m %H:%M", time.gmtime()))
print(eval(time.strftime("{'week': '%a', 'day': int('%d'), 'month': int('%m'), 'time': (int('%H'), int('%M'))}", time.gmtime())))

'''
%a - Сокращенное название дня недели
%A - Полное название дня недели
%b - Сокращенное название месяца
%B - Полное название месяца
%c - Дата и время
%d - День месяца [01,31]
%H - Час (24-часовой формат) [00,23]
%I - Час (12-часовой формат) [01,12]
%j - День года [001,366]
%m - Номер месяца [01,12]
%M - Число минут [00,59]
%p - До полудня или после (при 12-часовом формате)
%S - Число секунд [00,61]
%U - Номер недели в году (нулевая неделя начинается с воскресенья) [00,53]
%w - Номер дня недели [0(Sunday),6]
%W - Номер недели в году (нулевая неделя начинается с понедельника) [00,53]
%x - Дата
%X - Время
%y - Год без века [00,99]
%Y - Год с веком
%Z - Временная зона
%% - Знак '%'
'''