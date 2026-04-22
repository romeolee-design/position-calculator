def bprint(text):
    print()
    print('='* 5,'калькулятор позиции','=' * 5)
    print (text)
    print('='* 10)
    print()


def calculate(risk_percent, entry, stop, rr):
    deposit = 100000
    risk_amount = deposit * (risk_percent / 100)
    stop_distance = abs(entry - stop)
    if entry > stop:
        direction = 'LONG'
        take_profit = entry + (stop_distance * rr)
    elif entry == stop:
        print("Ошибка значений")
        return
    else:
        direction = 'SHORT'
        take_profit = entry - (stop_distance * rr)

    percent_move = (stop_distance / entry) * 100
    position_value = risk_amount / (percent_move / 100)
    bprint(f'Тип сделки: {direction}\nЦена входа:{entry:g}\nСтоп:{stop:g}\nРиск:{risk_percent:g} %\nРиск:{risk_amount:g} $\n% до стопа:{percent_move:g} \nОбъём позиции:{position_value:g} $\nТейк профит:{take_profit:g}')

while True:
    
    risk_percent = float(input('Риск в процентах: '))
    entry = float(input('Цена входа: '))
    stop = float(input('Стоп-лос: '))
    rr = float(input('Введите риск/прибыль (RR, например 2): '))

    calculate(risk_percent,entry,stop,rr)
