import csv
import re

def number(contacts_list):
    number_pattern_raw = r'(\+7|8)(\s*)(\(*)(\d{3})(\)*)(\s*)' \
                            r'(\-*)(\d{3})(\s*)(\-*)(\d{2})(\s*)(\-*)' \
                            r'(\d{2})(\s*)(\(*)(доб)*(\.*)(\s*)(\d+)*(\)*)'
    number_pattern_new = r'+7(\4)\8-\11-\14\15\17\18\19\20'
    contacts_list_updated = list()
    for card in contacts_list:
        print(card)
        card_as_string = ','.join(card)
        print(card_as_string)
        formatted_card = re.sub(number_pattern_raw, number_pattern_new, card_as_string)
        card_as_list = formatted_card.split(',')
        print(card_as_list)
        contacts_list_updated.append(card_as_list)

    return contacts_list_updated

def format_full_name(contacts_list):
  name_pattern_raw = r'^([А-ЯЁа-яё]+)(\s*)(\,?)([А-ЯЁа-яё]+)' \
                     r'(\s*)(\,?)([А-ЯЁа-яё]*)(\,?)(\,?)(\,?)'
  name_pattern_new = r'\1\3\10\4\6\9\7\8'
  contacts_list_updated = list()
  for card in contacts_list:
    card_as_string = ','.join(card)
    formatted_card = re.sub(name_pattern_raw, name_pattern_new, card_as_string)
    card_as_list = formatted_card.split(',')
    contacts_list_updated.append(card_as_list)
  return contacts_list_updated

def remove_duplicates(contacts_list):
    contacts_list_updated = []
    for i in contacts_list:
        for employee in contacts_list:
            if i[0:2] == employee[0:2]:
                list_employee = i
                i = list_employee[0:2]
                for j in range(2, 7):
                    if list_employee[j] == '':
                        i.append(employee[j])
                    else:
                        i.append(list_employee[j])
        if i not in contacts_list_updated:
            contacts_list_updated.append(i)
    return contacts_list_updated

if __name__ == '__main__':
    with open("phonebook_raw.csv", encoding='utf-8') as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)


    contacts_1 = number(contacts_list)
    contacts_2 = format_full_name(contacts_1)
    contacts_3 = remove_duplicates(contacts_2)

    with open("phonebook.csv", "w") as f:
      datawriter = csv.writer(f, delimiter=',')
      datawriter.writerows(contacts_3)


