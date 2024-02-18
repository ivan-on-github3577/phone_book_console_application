from functions import *


operation = ''

while operation != 'в':
    operation = input('☎Телефонный справочник📔\n    Введите действие:\nп - Показать все, с - Создать контакт,\nн - Найти контакт, и - Изменить контакт,\nу - Удалить контакт, к - Копировать контакт,\nв - Выход.\n')
    
    if operation == 'п':
        render_contacts()
    elif operation == 'с':
        inputed = inputing()
        add_contact(inputed[0], inputed[1], inputed[2])
        print(f'Контакт {inputed[0]} добавлен.')
    elif operation == 'н':
        print('Кого ищем?\nПостарайтесь написать имя в точности как в справочнике.')
        print('Если не знаете или хотите пропустить пункт ввода - введите пробел.')
        who_need = inputing()
        replace_spaces_with_none(who_need)
        print(*find_contact(who_need[0], who_need[1], who_need[2]))
    elif operation == 'и':
        print('Кого изменить?\nПостарайтесь написать в точности как в справочнике.')
        print('Если не знаете или хотите пропустить пункт ввода - введите пробел.')
        who_need = inputing()
        print(f'Введите новые данные для контакта {who_need[0]}.')
        who_will = inputing()
        replace_spaces_with_none(who_need)
        edit_contact(who_need[0], who_need[1], who_need[2],
                     who_will[0], who_will[1], who_will[2])
    elif operation == 'у':
        print('Кого удалить?\nПостарайтесь написать имя в точности как в справочнике.')
        who_need = inputing()
        replace_spaces_with_none(who_need)
        del_contact(who_need[0], who_need[1], who_need[2])
    elif operation == 'к':
        whence = input('Из какого файла копировать?\n')
        print('\nКого копировать?\nПостарайтесь написать в точности как в справочнике.')
        print('Если не знаете или хотите пропустить пункт ввода - введите пробел.')
        copyable_contact = inputing()
        replace_spaces_with_none(copyable_contact)
        copying_from_another(whence, copyable_contact[0],
                                     copyable_contact[1],
                                     copyable_contact[2])
    else:
        print('Вы вышли или сделали неправильный ввод. Можете попробовать заново.')





