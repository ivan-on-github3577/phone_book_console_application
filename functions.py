

def get_list_of_list_contacts(contacts):
    contacts = list(contacts)
    for i in range(len(contacts)):
        contacts[i] = contacts[i].split(';') # сделал список списков(каждый список в списке - контакт)
    return contacts

def render_contacts():
    with open ('phone book.txt', 'r', encoding='utf-8') as contacts:
        contacts = get_list_of_list_contacts(contacts)
        
        max_len_of_name_cell = 0
        max_len_of_phone_cell = 0
        max_len_of_comment_cell = 0
        for contact in contacts:
            if len(contact[0]) > max_len_of_name_cell:
                max_len_of_name_cell = len(contact[0])
            if len(contact[1]) > max_len_of_phone_cell:
                max_len_of_phone_cell = len(contact[1])
            if len(contact[2]) > max_len_of_comment_cell:
                max_len_of_comment_cell = len(contact[2])

        for contact in contacts:
            if len(contact[0]) < max_len_of_name_cell:
                contact[0] = contact[0] + ' '*(max_len_of_name_cell - len(contact[0]))
            if len(contact[1]) < max_len_of_phone_cell:
                contact[1] = contact[1] + ' '*(max_len_of_phone_cell - len(contact[1]))
            if len(contact[2]) < max_len_of_comment_cell:
                contact[2] = contact[2] + ' '*(max_len_of_comment_cell - len(contact[2]))

        for_print = []
        for contact in contacts:
            for cell in contact:
                for_print.append(cell)

            
        print(*for_print)






def add_contact(name, phone, comment='-'):
    with open ('phone book.txt', 'a', encoding='utf-8') as contacts:
        contacts.writelines([name+';', phone+';', comment+';\n'])




def find_contact(name=None, phone=None, comment=None,
                 contact_only=True, path='phone book.txt'):
    with open (path, 'r', encoding='utf-8') as contacts:
        contacts = get_list_of_list_contacts(contacts)
        for contact_index in range(len(contacts)-1):
            current_contact = contacts[contact_index]
            for i in range(len(current_contact)):
                if current_contact[i] == name or current_contact[i] == phone or current_contact[i] == comment:
                    if contact_only == False:
                        return (contact_index, contacts)
                    else:
                        return contacts[contact_index]




def del_contact(name=None, phone=None, comment=None):
    editing_bufer = find_contact(name, phone, comment, False)
    del editing_bufer[1][editing_bufer[0]]

    with open ('phone book.txt', 'w', encoding='utf-8') as contacts:
        for contact in editing_bufer[1]:
            for element in contact:
                if element[-2:] != '\n':
                    contacts.write(element+';')
                elif element[-2:] == '\n':
                    contacts.write(element)

                


def edit_contact(old_name=None, old_phone=None, old_comment=None,
                 new_name='-', new_phone='-', new_comment='-'):
    editing_bufer = find_contact(old_name, old_phone, old_comment, False)

    editing_bufer[1][editing_bufer[0]] = [new_name, new_phone, new_comment, '\n']

    with open ('phone book.txt', 'w', encoding='utf-8') as contacts:
        for contact in editing_bufer[1]:
            for element in contact:
                if element[-2:] != '\n':
                    contacts.write(element+';')
                elif element[-2:] == '\n':
                    contacts.write(element)




def inputing():
    name = input('Введите имя: ')
    phone = input('Введите номер телефона: ')
    comment = input('Введите комментарий: ')
    return (name, phone, comment)




def copying_from_another(whence, name=None, phone=None, comment=None):
    copyable_contact = find_contact(name, phone, comment, True, whence)
    print(copyable_contact)