# Урок 1. Задание 5.
r = int(input('Укажите выручку ООО Рога и Копыта за 2022г '))
tc = int(input('Укажите издержки ООО Рога и Копыта за 2022г '))
profit = r - tc
edc = abs(tc - r)
if profit > 0:
    print('Поздравляем Ваша прибыль за 2022г. составила', profit, 'Не забудьте заплатить налоги')
else:
    if profit == 0:
        print('все не так плохо Вы в нуле')
    else:
        print('К сожалению Ваш убыток в 2022г. составил', edc, 'В нефтьаламазбанке низкая ставка по кредитам')
