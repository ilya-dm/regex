import re
from pprint import pprint

import csv
def open_csv():
    with open("phonebook.csv", encoding='utf-8') as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
    return contacts_list

def regex():
    raw_text = open_csv()
    format_text = list()
    pattern1 = re.compile(r'^([А-Я]\w+)(\s|,)([А-Я]+\w+)(\s|,)([А-Я]+\w+|\s*)(,{2,3})')
    pattern2 = re.compile('(8|\+7)(\s*)(\(|\s*)(\d{3})(\)|\s*)(\s*|-)(\d{3})(\s*|-)(\d{2})\
    (\s*|-)(\d{2})(\s*)(\(|\s*)(\w*)(\.*)(\s*)(\d*)(\)|\s*)')
    sub1 = r"\1,\3,\5,"
    sub2 = r'+7(\4)\7-\9-\11\12\14\15\17'
    for contact in raw_text:
        b = ','.join(contact)
        b = pattern1.sub(sub1, b)
        b = pattern2.sub(sub2, b)
        b = b.split(',')
        format_text.append(b)
    return format_text
def del_double():
    raw_text = regex()
    d = dict()
    for contact in raw_text:
        if contact[0] not in d:
            d[contact[0]] = contact
        else:
            for index in range(0, len(contact)):
                if contact[index] not in d[contact[0]] and d[contact[0]][index] == '':
                    d[contact[0]][index] = contact[index]
                elif contact[index] not in d[contact[0]] and d[contact[0]][index] != '':
                    d[contact[0]][index+1] = contact[index]


    return d
def new_file():
    contacts_dict = del_double()
    contacts_list = list()
    for contact in contacts_dict:
        contacts_list.append(contacts_dict[contact])

    with open("phonebook_new.csv", "w") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(contacts_list)

if __name__ == '__main__':
    new_file()