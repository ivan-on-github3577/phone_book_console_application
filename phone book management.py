from functions import *


operation = ''

while operation != 'в':
    operation = input('☎Телефонный справочник📔\n    Введите действие:\nп - Показать все, с - Создать контакт,\nн - Найти контакт, и - Изменить контакт,\nу - Удалить контакт, в - Выход.\n')
    
    if operation == 'п':
        render_contacts()
    elif operation == 'с':
        inputed = inputing()
        add_contact(inputed[0], inputed[1], inputed[2])
        print(f'Контакт {inputed[0]} добавлен.')
    elif operation == 'н':
        print('Кого ищем?\nПостарайтесь написать имя в точности как в справочнике.')
        who_need = input('Введите имя: ')
        print(*find_contact(who_need))
    elif operation == 'и':
        print('Кого изменить?\nПостарайтесь написать в точности как в справочнике.')
        who_need = inputing()
        print(f'Введите новые данные для контакта {who_need[0]}.')
        who_will = inputing()
        edit_contact(who_need[0], who_need[1], who_need[2],
                     who_will[0], who_will[1], who_will[2])
    elif operation == 'у':
        print('Кого удалить?\nПостарайтесь написать имя в точности как в справочнике.')
        who_need = input('Введите имя: ')
        del_contact(who_need)
    else:
        print('Вы вышли или сделали неправильный ввод. Можете попробовать заново.')





# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ блок для проверок ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# render_contacts()

# add_contact('Маша', '252525')
# print(*find_contact('Оля Ля')) # выведет контакт "Оля Ля"
# edit_contact('Юля Красотуля', '+79993332288', 'всегда накрашена', 'Юля Красотуля', 'потеряла телефон')

# del_contact('Маша') # проблема в том,что не удаляет контакт если это последний контакт в "phone book.txt",
                      # не могу понять почему так...


# add_contact('Вика', '525252')
# теперь Маша предпоследняя и удалится
# del_contact('Маша')

# render_contacts()