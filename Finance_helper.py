

from datetime import datetime
from copy import deepcopy


time_encrypt = datetime.now().strftime('%c')          # переменная времени
time_encrypt = time_encrypt[-4:] + time_encrypt[3:-4] # нужный мне формат

start=''#
while True:
    start=input('''
Hello. I can help you with your income and expenses!!!

If you need my help write me         : (1)
If want finish program write me      : (0)
''')


    if start == '1':
        income_expenses=input('''
Write me your income and expenses!

Please use only this form 
Category(income_or_expenses):category(supplies_or_salary_or_other):Sum_money, ''')   #Прошу ввести список расходов\доходов

        date = ('No_info','Income', 'Expenses', time_encrypt, 'Report about Income/Expenses !!!','Average expenses:', 'Average income:','Other','Result')


        income_expenses=income_expenses.split(', ')   #Превращаю строку в список исходя из запятой с пробелом

        i                = 0           #переменная для цыклов обнуляю ее после кажого цыкла

        income           = []          #список с доходами

        income_sum       = 0

        income_min       = '-'

        income_max       = '-'

        expenses         = []          #список с расходами

        expenses_sum     = 0

        expenses_max     ='-'

        expenses_min     ='-'

        other            = []          #список с не понятными данными (указанные не верно)

        average_expenses = '-'           #переменная среднего расхода

        average_income   = '-'           #переменная среднего дохода

        while len(income_expenses) > i: # превращаем в подсписки так же приводим к стандарту из трех элементов
            in_ex=income_expenses[i].split(':')
            if len(in_ex)==2:
                in_ex[1:1]=[date[0]]

            income_expenses[i] = in_ex
            i += 1

        if len(income_expenses)>=1 and len(income_expenses[0])>=2:
            income_expenses=[[sublist[0].capitalize(), sublist[1].capitalize(),
                          float(sublist[2]) if sublist[2].replace(',','')
                          .replace('.','').isdigit() else date[0]] for sublist in income_expenses]
        else:
            print("\nYou haven't entered any information for analise! Try again!!! ")
            continue


        i=0
        while len(income_expenses)  > i:#сортируем список на три других
            if income_expenses[i][0].lower()==date[1].lower():
                income.append(deepcopy(income_expenses[i][0:]))

            elif income_expenses[i][0].lower()==date[2].lower():
                expenses.append(deepcopy(income_expenses[i][0:]))

            else:
                other.append(deepcopy(income_expenses[i][0:]))
            i+=1


        if len(income)>0:
            income_max      = max(sublist[2] for sublist in income)
            income_min      = min(sublist[2] for sublist in income)
            income_sum      = sum(sublist[2] for sublist in income)
            average_income  = income_sum / len(income)

        if len(expenses)>0:
            expenses_max      = max(sublist[2] for sublist in expenses)
            expenses_min      = min(sublist[2] for sublist in expenses)
            expenses_sum      = sum(sublist[2] for sublist in expenses)
            average_expenses  = expenses_sum / len(expenses)

        total_balance        =  income_sum    - expenses_sum                    # узнаем общй баланс
        number_of_operation  =  len(expenses) + len(income)            # общ кол операций


        income_str=('\n'.join(' | '.join(map(str, sublist)) for sublist in income)).replace('\n', '$\n')
        expenses_str='\n'.join(' | '.join(map(str, sublist)) for sublist in expenses).replace('\n', '$\n')
        other_str='\n'.join(' | '.join(map(str,sublist))for sublist in other ).replace('\n', '$\n')
        if len(income_str)>0:
            income_str+='$'
        else:
            income_str='No_info !!!!!'
        if len(expenses_str)>0:
            expenses_str+='$'
        else:
            expenses_str = 'No_info !!!!!'
        if len(other_str) > 0:
            other_str += '$'
        else:
            other_str = 'No_info !!!!!'

        text=f'''
\n{date[4]:_^40}\n
Date & Time : {date[3]:=^26}\n\n\
{date[1]:-^40}\n\n{income_str}\n\nTotal income: {income_sum}$\nIncome max: {income_max}$\nIncome min: {income_min}$\n{date[6]} {average_income}$
\n{date[2]:-^40}\n\n{expenses_str}\n\nTotal expenses: {expenses_sum}$\nExpenses max: {expenses_max}$\nExpenses min: {expenses_min}$\n{date[5]} {average_expenses}$
\n{date[7]:-^40}\n\n{other_str}\n\n
{date[8]:-^40}\n\nTotal Balance: {total_balance}$\nIncome number of operation: {len(income)}\nExpenses number of operation:{len(expenses)}
Total number of operation: {number_of_operation}'''

        open('finance_report.txt','a+', encoding='utf-8').write('\n'*7+ text)

        print(text)

    elif start == '0':
        print('Program completed! Goodbye!!!')

    else: continue
    start=""
