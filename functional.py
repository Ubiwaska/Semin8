path = "phone_book.txt"
def print_records(file_name: str):
    with open(file_name, 'r', encoding='utf-8') as data:
        for line in data:
            print(*line.split(' '), end=' ')

def input_records(file_name: str):
    with open(file_name, 'r+', encoding='utf-8') as data:
        record_id = 0
        for line in data:
            if line != ' ':
                record_id = line.split(' ', 1)[0]
        print('Введите данные абонента')
        print()
        line = f'{int(record_id) + 1} ' + ' '.join(input().split()[:4]) + ';\n'
        # input('Введите данные абонента \n').split()[:4] + ';\n'   
        confirm = input(f"Вносим новые данные: y - да, n - нет\n")
        while confirm not in ('y', 'n'):
            print('Неверные данные')
        if confirm == 'y':
            data.write(line)
        return

def find_char():
    print('Поиск по: 0 - Id, 1 - Фамилии, q - quit')
    print()
    char = input('выберите действие  ')
    print()
    while char not in ('0', '1', 'q'):
    #     # print('Неверные данные')
    #     # print('Choose char: ')
    #     # print('0 - id, 1 - second name, 2 - first name, 3 - third name, 4 - number, q - quit')
        char = input("выберите действие ")
    if char != 'q':
        if char == "0" : inp = input('Введите Id контакта - ')
        elif char == "1": inp = input('Введите Фамилию контакта - ')
        else: print('Данный параметр неиспользуется')
        print()
        return char, inp
    else:   
        return 'q', 'q'
    
def find_records(file_name: str, char, condition):
    if condition != 'q':
        printed = False
        with open(file_name, 'r', encoding='utf-8') as data:
            for line in data:
                if condition == line.split(' ')[int(char)]:
                    print()
                    print('контакт найден :')
                    print(*line.split(' '))
                    printed = True
        if not printed:
            print("Такого контакта нет")
        return printed

def check_id_record(file_name: str, text: str):
    decision = input(f'Удалить? 1 - да, 2 - нет, q - выход\n')
    while decision not in ('1', 'q'):
        if decision != '2':
            print('Данный параметр неиспользуется')
        else:
            find_records(path, *find_char())
        decision = input(f'D u know id? {text}? 1 - yes, 2 - no, q - quit\n')
    if decision == '1':
        record_id = input('Введите id, q - выход\n')
        while not find_records(file_name, '0', record_id) and record_id != 'q':
            record_id = input('Введите id, q - выхд\n')
        return record_id
    return decision

def replace_record_line(file_name: str, record_id, replaced_line: str):
    replaced = ''
    with open(file_name, 'r', encoding='utf-8') as data:
        for line in data:
            replaced += line
            if record_id == line.split(' ', 1)[0]:
                replaced = replaced.replace(line, replaced_line)
    with open(file_name, 'w', encoding='utf-8') as data:
        data.write(replaced)

def change_records(file_name: str):
    record_id = check_id_record(file_name, 'change')
    if record_id != 'q':
        replaced_line = f'{int(record_id)} ' + ' '.join(
            input('Введите новые данные контакта \n').split()[:4]) + ';\n'   
        confirm = input(f"Вносим изменения: y - да, n - нет\n")
        while confirm not in ('y', 'n'):
            print('Неверные данные')
        if confirm == 'y':
            replace_record_line(file_name, record_id, replaced_line)

def delete_records(file_name: str):
    record_id = check_id_record(file_name, 'delete')
    if record_id != 'q':
        replace_record_line(file_name, record_id, '')