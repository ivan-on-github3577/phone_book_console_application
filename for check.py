from functions import *


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ блок для проверок ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# render_contacts()

# add_contact('Маша', '252525')
# print(*find_contact('Оля Ля')) # выведет контакт "Оля Ля"
# edit_contact('Юля Красотуля', '+79993332288', 'всегда накрашена', 'Юля Красотуля', 'потеряла телефон')

# del_contact('Маша') # проблема в том,что не удаляет контакт если это последний контакт(загвоздка в функции "find_contact()"),
                      # не могу понять почему так...


# add_contact('Вика', '525252')
# теперь Маша предпоследняя и удалится
# del_contact('Маша')

copying_from_another('copyable phone_book.txt', 'Марина')

# render_contacts()