from start_pack.functions.get_random_number import get_random_number


def create_book():
    '''
    Получаем книгу в виде словаря
    :return:
    '''
    print('Введите название книги')
    book_name = input()
    print('Укажите имя втора')
    book_author = input()
    print('Укажите год')
    book_year = input()
    book = dict()
    book['book_name'] = book_name
    book['book_author'] = book_author
    book['book_year'] = book_year
    book['book_id'] = get_random_number()  # получаем уникальный book_id
    book['book_status'] = 'в наличии'
    print('Книга успешно добавлена...\n')
    return book
