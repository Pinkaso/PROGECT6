def debt(cost,years,percent):
    i = 0
    percent = percent / 100
    while i != years:
        cost += cost * percent
        i += 1
    print('Через {} лет вам нужно будет выплатить - {} рублей.'.format(years,cost))

def month(cost,years):
    one_month = round((cost / (12 * years)),2)
    print('Каждый месяц вам нужно откладывать ~ {} рублей.'.format(one_month))

def ans(answer,cost,years):
    if answer.lower() == 'да' or answer.lower() == 'yes' or answer.lower() == '+':
        month(cost, years)
    else:
        print('Спасибо за то, что были с нами!')

def main():
    cost = int(input('Введите стоимость автомобиля: '))
    years = int(input('На сколько лет вы хотите взять кредит? Введите: '))
    percent = int(input('Какие проценты, установленные банком? Введите: '))
    debt(cost,years,percent)
    answer = input('Хотите узнать сколько вам нужно откладывать каждый месяц, чтобы вернуть долг вовремя? Ваш ответ: ')
    ans(answer,cost,years)


if __name__ == '__main__':
    main()