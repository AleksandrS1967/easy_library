from random import randint
import start_pack

def get_random_number():
    '''
    Получаем рандомный book_id проверив его уникальность
    :return:
    '''
    check_list = list()
    list_books = start_pack.work_with_json.get_data(start_pack.data_book_path)
    if list_books:
        [check_list.append(i['book_id']) for i in list_books]
    random_number = "".join([str(randint(0, 9)) for i_ in range(8)])
    if random_number not in check_list:
        return random_number
    else:
        return str(int(random_number) + int("".join([str(randint(0, 9)) for i_ in range(8)])))