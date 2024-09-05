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
        
    return (new_lastname, new_firstname, new_surname)

def convert_phone(phone:str):
    pattern = r'(\+7|8)?\s*\((\d+)\)\s*(\d+)[\s-]*(\d+)[\s-]*(\d+)'

def main():
    # читаем адресную книгу в формате CSV в список contacts_list
    with open("phonebook_raw.csv", encoding="utf-8") as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
    pprint(contacts_list)

    # TODO 1: выполните пункты 1-3 ДЗ
    new_list = []
    new_list.append(contacts_list[0])
    for lastname, firstname, surname, organization, position, phone, email in contacts_list[1:]:
        new_lastname, new_firstname, new_surname = convert_names(lastname, firstname, surname)
        pass


    # TODO 2: сохраните получившиеся данные в другой файл
    # код для записи файла в формате CSV
    with open("phonebook.csv", "w", encoding="utf-8") as f:
        datawriter = csv.writer(f, delimiter=',')
        # Вместо contacts_list подставьте свой список
        datawriter.writerows(contacts_list)

if __name__ == '__main__':
    main()