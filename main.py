from pprint import pprint
import csv

import re

def convert_names(lastname:str, firstname:str, surname:str)->tuple:
    new_surname = surname.split()
    new_firstname = firstname.split()
    new_lastname = lastname.split()
    if len(new_lastname) == 1:
        new_lastname = lastname
    elif len(new_lastname) == 2:
        new_firstname = new_lastname[1]
        new_lastname = new_lastname[0]
    elif len(new_lastname) == 3:
        new_surname = new_lastname[2]
        new_firstname = new_lastname[1]
        new_lastname = new_lastname[0]

    
    if len(new_firstname) == 1:
        new_firstname = firstname
    elif len(new_firstname) == 2:
        new_surname = new_firstname[1]
        new_firstname = new_firstname[0]
    
    if len(new_surname) <= 1:
        new_surname = surname
        
    return (new_lastname, new_firstname, new_surname)

def repl_phone(match):
    return f'+7({match['city']}){match['first']}-{match['second']}-{match['third']}' + (f' доб. {match['add']}' if match['add'] != None else '')

def convert_phone(phone:str):
    pattern = r"(?P<country>\+7|8)\s*\(*(?P<city>\d\d\d)\)*\s*\-*(?P<first>\d\d\d)\s*\-*(?P<second>\d\d)\s*\-*(?P<third>\d\d)\s*\(*д*о*б*\.*\s*(?P<add>\d\d\d\d)*\)*"
    return re.sub(pattern, 
                repl_phone, 
                phone)

def unification_dict(old_dict:dict, new_dict:dict)->dict:
    if new_dict['lastname'] == '':
        new_dict['lastname'] = old_dict['lastname']
    if new_dict['firstname'] == '':
        new_dict['firstname'] = old_dict['firstname']
    if new_dict['surname'] == '':
        new_dict['surname'] = old_dict['surname']
    if new_dict['organization'] == '':
        new_dict['organization'] = old_dict['organization']
    if new_dict['position'] == '':
        new_dict['position'] = old_dict['position']
    if new_dict['phone'] == '':
        new_dict['phone'] = old_dict['phone']
    if new_dict['email'] == '':
        new_dict['email'] = old_dict['email']
    return new_dict

def main():
    # читаем адресную книгу в формате CSV в список contacts_list
    with open("phonebook_raw.csv", encoding="utf-8") as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
    pprint(contacts_list)

    # TODO 1: выполните пункты 1-3 ДЗ
    new_list = []
    new_list.append(contacts_list[0])
    phonebook_dict = {}
    for lastname, firstname, surname, organization, position, phone, email in contacts_list[1:]:
        new_lastname, new_firstname, new_surname = convert_names(lastname, firstname, surname)
        new_phone = convert_phone(phone)
        if new_lastname + new_firstname in phonebook_dict:
            phonebook_dict[new_lastname+new_firstname] = unification_dict(
                phonebook_dict[new_lastname+new_firstname],
                {'lastname': new_lastname,
                'firstname': new_firstname,
                'surname' : new_surname,
                'organization': organization,
                'position' : position,
                'phone': new_phone,
                'email' : email}
            )
        else:
            phonebook_dict[new_lastname+new_firstname] = {
                'lastname': new_lastname,
                'firstname': new_firstname,
                'surname' : new_surname,
                'organization': organization,
                'position' : position,
                'phone': new_phone,
                'email' : email
            }

    for value in phonebook_dict.values():
        new_list.append([value['lastname'], value['firstname'], value['surname'], value['organization'], value['position'], value['phone'], value['email']])
    # TODO 2: сохраните получившиеся данные в другой файл
    # код для записи файла в формате CSV
    with open("phonebook.csv", "w", encoding="utf-8") as f:
        datawriter = csv.writer(f, delimiter=',')
        # Вместо contacts_list подставьте свой список
        datawriter.writerows(new_list)

if __name__ == '__main__':
    main()