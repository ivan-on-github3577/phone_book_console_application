import view
from model import PhoneBook
import text





def start_app():
    pb = PhoneBook()
    confirm_accept = view.Confirm()
    while True:
        user_choice = view.show_main_menu()
        match user_choice:
            case 1:
                pb.open_phone_book()
                view.show_message(text.phone_book_opened_successful)
            case 2:
                pb.save_phone_book()
                view.show_message(text.phone_book_saved_successful)
            case 3:
                view.show_contacts(pb.phone_book, text.empty_phone_book_error)
            case 4:
                new_contact = view.input_data(text.input_new_contact)
                pb.add_new_contact(new_contact)
                view.show_message(text.new_contact_added_successful(new_contact[0]))
            case 5:
                pb.find_contacts(view.input_data, view.show_contacts,
                                 text.input_search_word, text.find_contact_no_result)
            case 6:
                if pb.find_contacts(view.input_data, view.show_contacts,
                                 text.input_search_word_for_edit, text.find_contact_no_result):
                    u_id = int(view.input_data(text.input_id_for_edit))
                    edited_contact = view.input_data(text.edit_contact)
                    name = pb.edit_contact(u_id, edited_contact)
                    view.show_message(text.edit_contact_successful(name))
            case 7:
                if pb.find_contacts(view.input_data, view.show_contacts,
                                 text.input_search_word_for_delete, text.find_contact_no_result):
                    u_id = int(view.input_data(text.input_id_for_delete))
                    if confirm_accept.confirm(text.confirm_on_delete, text.confirm_on_delete_accept):
                        name = pb.delete_contact(u_id)
                        view.show_message(text.delete_contact_successful(name))
            case 8:
                if pb.on_exit():
                    if confirm_accept.confirm(text.exit_changes, text.exit_confirm):
                        pb.save_phone_book()
                        view.show_message(text.exit_no_changes + ' ' + text.exit_no_changes_confirm)
                    else:
                        view.show_message(text.exit_no_changes + ' ' + text.exit_no_changes_no_confirm)
                else:
                    view.show_message(text.exit_no_changes)
                break